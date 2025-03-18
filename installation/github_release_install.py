# @Author: Kristinita
# @Date: 2025-03-17 20:26:53
# @Last Modified by: SashaChernykh
# @Last Modified time: 2025-03-18 21:41:28
"""[OVERVIEW] Install non-Node and non-Python binaries from GitHub releases.

######################
# gh-release-install #
######################
[OVERVIEW] gh-release-install — Python CLI utility for installation data from GitHub releases.
https://github.com/jooola/gh-release-install

[PURPOSE] Amazing Grace is the Node.js + Python project, but it also uses dependencies
that not possible to install use Node.js and Python.
One of the main principles of Amazing Grace is simplicity.
So that users don’t have to pre-install any dependencies except Git, Node.js and Python,
I installed non-Node and non-Python CLI dependencies use gh-release-install.

[INFO] gh-release-install save binaries from GitHub releases to the PATH directory of Pipenv virtual environment.
To launch commands, the user should use the syntax “pipenv run command”,
for example, “pipenv run fd” or “pipenv run tidy”.


[NOTE] gh-release-install hasn’t configuration file, “github_release_install.py” script is required:
https://github.com/jooola/gh-release-install/issues/212

[NOTE] As of March 2025, I can’t find good cross-platform package manager for GitHub releases.
“fetch-github-release” and “install-release” doesn’t support Windows:
https://github.com/terascope/fetch-github-release/issues/355
https://github.com/Rishang/install-release
I can’t run “grab-github-release”:
https://github.com/prantlf/grab-github-release/issues/2
"""
import subprocess
import sys
import os

# [LEARN][PYTHON] “sys.platform” — check current operating system.
# Windows always has the value “win32”, macOS — “darwin”, Linux — “linux”:
# https://docs.python.org/3/library/sys.html#sys.platform
KIRA_PLATFORM_MACOS = "darwin"
KIRA_PLATFORM_WINDOWS = "win32"


def kira_save_binaries_from_github_releases():
    """[FUNCTION_DESCRIPTION] Save non-Node/non-Python binaries from GitHub releases into Pipenv virtual environment.

    Steps:
    -----

    1. Set gh-release-install commands.
    2. Run gh-release-install commands.
    3. Exit “github_release_install.py” with the same exit code as exit codes of gh-release-install commands.
    """
    kira_current_os_is_windows = sys.platform == KIRA_PLATFORM_WINDOWS
    kira_current_os_is_macos = sys.platform == KIRA_PLATFORM_MACOS

    # [NOTE] Pipenv has different paths for executable binaries for Linux/macOS and Windows.
    # “.venv/bin” — is the path for Linux and macOS, “.venv/Scripts” — the path for Windows.
    kira_destination_path = ".venv/Script" if kira_current_os_is_windows else ".venv/bi"

    # [PURPOSE] Save binaries from unofficial HTML Tidy 5.9.20 release:
    # https://github.com/Kristinita/tidy-html5/releases/tag/5.9.20
    # Release contains solely binaries, not archives.
    #
    # [NOTE] I created my own HTML Tidy release, because Tidy is no longer maintained,
    # and the latest official Tidy versions contains critical bugs:
    # https://github.com/Kristinita/tidy-html5#2-why-it-was-created
    #
    #
    # [INFO] Linux and macOS CLI command:
    # gh-release-install Kristinita/tidy-html5 tidy .venv/bin --verbose
    #
    # Windows CLI command:
    # gh-release-install Kristinita/tidy-html5 tidy.exe .venv/Scripts --verbose
    kira_tidy_repository = "Kristinita/tidy-html5"
    kira_tidy_executable_file = "tidy.exe" if kira_current_os_is_windows else "tidy"

    kira_gh_release_install_command_for_tidy = [
        "pipenv", "run", "gh-release-install",
        kira_tidy_repository,
        kira_tidy_executable_file,
        kira_destination_path,
        "--verbose"
    ]

    # [PURPOSE] Save binaries from the latest fd release:
    # https://github.com/sharkdp/fd/releases
    # Archives unpacking is required.
    #
    #
    # [INFO] Linux CLI command:
    # gh-release-install sharkdp/fd "fd-{tag}-x86_64-unknown-linux-gnu.tar.gz"
    # --extract "fd-{tag}-x86_64-unknown-linux-gnu/fd" .venv/bin/fd --verbose
    #
    # [INFO] macOS CLI command:
    # gh-release-install sharkdp/fd "fd-{tag}-x86_64-apple-darwin.tar.gz"
    # --extract "fd-{tag}-x86_64-apple-darwin.tar.gz/fd" .venv/bin/fd --verbose
    #
    # [INFO] Windows CLI command:
    # gh-release-install sharkdp/fd fd-{tag}-x86_64-pc-windows-gnu.zip
    # --extract fd-{tag}-x86_64-pc-windows-gnu/fd.exe .venv/Scripts/fd.exe --verbose
    kira_fd_repository = "sharkdp/fd"
    kira_fd_executable_file = "fd"

    if kira_current_os_is_windows:
        kira_fd_archive = "fd-{tag}-x86_64-pc-windows-gnu.zip"
        kira_fd_extract = "fd-{tag}-x86_64-pc-windows-gnu/fd.exe"
        kira_fd_executable_file = "fd.exe"

    elif kira_current_os_is_macos:
        kira_fd_archive = "fd-{tag}-x86_64-apple-darwin.tar.gz"
        kira_fd_extract = "fd-{tag}-x86_64-apple-darwin/fd"

    else:
        kira_fd_archive = "fd-{tag}-x86_64-unknown-linux-gnu.tar.gz"
        kira_fd_extract = "fd-{tag}-x86_64-unknown-linux-gnu/fd"

    kira_gh_release_install_command_for_fd = [
        "pipenv", "run", "gh-release-install",
        kira_fd_repository,
        kira_fd_archive,
        "--extract",
        kira_fd_extract,
        os.path.join(kira_destination_path, kira_fd_executable_file),
        "--verbose"
    ]

    # [PURPOSE] Run gh-release-install commands
    #
    # [NOTE][PYLINT] Use “subprocess.Popen” with “with” keyword to avoid “R1732” Pylint warning:
    # https://pylint.pycqa.org/en/latest/user_guide/messages/refactor/consider-using-with.html
    with subprocess.Popen(
            kira_gh_release_install_command_for_tidy) as kira_tidy_process, subprocess.Popen(
            kira_gh_release_install_command_for_fd) as kira_fd_process:

        # [PURPOSE][LEARN][PYTHON] Wait until subprocesses are finished:
        # https://stackoverflow.com/a/15108096/5951529
        # https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait
        kira_tidy_process.wait()
        kira_fd_process.wait()

        # [PURPOSE][NOTE] “github_release_install.py” exits with exit code 0, if we’re not processing exit codes.
        # Desired behavior — if “kira_tidy_process” and/or “kira_fd_process” exited with non-zero exit code,
        # “github_release_install” should also exit with non-zero exit code.
        # The code below realize this behavior.
        #
        # [LEARN][PYTHON] “returncode” — get exit code of a subprocess:
        # https://stackoverflow.com/a/5631819/5951529
        kira_tidy_exit_code = kira_tidy_process.returncode
        kira_fd_exit_code = kira_fd_process.returncode

        if kira_tidy_exit_code != 0:
            print(f"Error: Tidy installation failed with exit code {kira_tidy_exit_code}")
        if kira_fd_exit_code != 0:
            print(f"Error: Fd installation failed with exit code {kira_fd_exit_code}")

        if kira_tidy_exit_code != 0 or kira_fd_exit_code != 0:

            # [LEARN][PYTHON][NOTE] “sys.exit()”, not “exit()” should be used in real Python scripts:
            # https://stackoverflow.com/a/6501134/5951529
            # https://stackoverflow.com/a/19747557/5951529
            sys.exit(1)
        else:
            sys.exit(0)


kira_save_binaries_from_github_releases()
