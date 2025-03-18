"""Kira Goddess."""
import subprocess
import sys
import os

# Define platform constants to replace magic strings
PLATFORM_WINDOWS = "win32"
PLATFORM_MACOS = "darwin"


def main():
    """Run two commands in parallel to install tidy-html5."""
    is_windows = sys.platform == PLATFORM_WINDOWS
    is_macos = sys.platform == PLATFORM_MACOS

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
    fd_output_executable_name = "fd"  # Default for non-Windows

    if is_windows:
        # Windows-specific values
        fd_archive_name = "fd-{tag}-x86_64-pc-windows-gnu.zip"
        fd_extract_path = "fd-{tag}-x86_64-pc-windows-gnu/fd.exe"
        fd_output_executable_name = "fd.exe"  # Override default
    elif is_macos:
        # macOS-specific values
        fd_archive_name = "fd-{tag}-x86_64-apple-darwin.tar.gz"
        fd_extract_path = "fd-{tag}-x86_64-apple-darwin/fd"
    else:  # Linux
        # Linux-specific values
        fd_archive_name = "fd-{tag}-x86_64-unknown-linux-gnu.tar.gz"
        fd_extract_path = "fd-{tag}-x86_64-unknown-linux-gnu/fd"

    # Build the command for installing fd (inline the output path)
    command_fd = [
        "pipenv", "run", "gh-release-install",
        fd_repository,
        fd_archive_name,
        "--extract",
        fd_extract_path,
        os.path.join(tidy_output_directory, fd_output_executable_name),
        "--verbose"
    ]

    # Use `with` statement for both Popen instances to avoid resource leaks
    with subprocess.Popen(command_tidy) as process_tidy, subprocess.Popen(command_fd) as process_fd:
        # Wait for both processes to complete
        process_tidy.wait()
        process_fd.wait()

        # Check return codes and handle errors
        tidy_return_code = process_tidy.returncode
        fd_return_code = process_fd.returncode

        if tidy_return_code != 0:
            print(f"Error: Tidy installation failed with exit code {tidy_return_code}")
        if fd_return_code != 0:
            print(f"Error: Fd installation failed with exit code {fd_return_code}")

        # Exit with non-zero if any command failed
        if tidy_return_code != 0 or fd_return_code != 0:
            sys.exit(1)
        else:
            sys.exit(0)


if __name__ == "__main__":
    main()
