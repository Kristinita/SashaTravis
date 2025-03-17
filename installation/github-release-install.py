"""Install binaries via gh-release-install."""
# @Author: SashaChernykh
# @Date: 2025-03-17 20:26:53
# @Last Modified by: SashaChernykh
# @Last Modified time: 2025-03-17 20:28:58
import subprocess
import sys
import os


def main():
    """Run two commands in parallel to install tidy-html5 and fd using gh-release-install via pipenv."""
    is_windows = sys.platform == 'win32'

    # Configure parameters for the tidy-html5 installation command
    tidy_repository = "Kristinita/tidy-html5"
    tidy_output_filename = "tidy.exe" if is_windows else "tidy"
    tidy_output_directory = ".venv/Scripts" if is_windows else ".venv/bin"

    # Build the command for installing tidy-html5
    command_tidy = [
        "pipenv", "run", "gh-release-install",
        tidy_repository,
        tidy_output_filename,
        tidy_output_directory,
        "--verbose"
    ]

    # Configure parameters for the fd installation command
    fd_repository = "sharkdp/fd"
    fd_archive_name = (
        "fd-{tag}-x86_64-pc-windows-gnu.zip" if is_windows else
        "fd-{tag}-x86_64-unknown-linux-gnu.tar.gz"
    )
    fd_extract_path = (
        "fd-{tag}-x86_64-pc-windows-gnu/fd.exe" if is_windows else
        "fd-{tag}-x86_64-unknown-linux-gnu/fd"
    )
    fd_output_executable_name = "fd.exe" if is_windows else "fd"
    fd_output_path = os.path.join(tidy_output_directory, fd_output_executable_name)

    # Build the command for installing fd
    command_fd = [
        "pipenv", "run", "gh-release-install",
        fd_repository,
        fd_archive_name,
        "--extract",
        fd_extract_path,
        fd_output_path,
        "--verbose"
    ]

    # Start both processes in parallel
    process_tidy = subprocess.Popen(command_tidy)
    process_fd = subprocess.Popen(command_fd)

    # Wait for both processes to complete
    process_tidy.wait()
    process_fd.wait()


if __name__ == "__main__":
    main()
