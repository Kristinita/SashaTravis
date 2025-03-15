@REM @Author: SashaChernykh
@REM @Date: 2025-03-15 15:20:41
@REM @Last Modified by: SashaChernykh
@REM @Last Modified time: 2025-03-15 16:39:42
START /B CMD /C "pipenv run gh-release-install Kristinita/tidy-html5 tidy.exe %APPVEYOR_BUILD_FOLDER%/.venv/Scripts --verbose"

START /B CMD /C "pipenv run gh-release-install sharkdp/fd fd-{tag}-x86_64-pc-windows-gnu.zip --extract fd-{tag}-x86_64-pc-windows-gnu/fd.exe %APPVEYOR_BUILD_FOLDER%/.venv/Scripts/fd.exe --verbose"
