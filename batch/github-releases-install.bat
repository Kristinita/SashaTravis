@REM @Author: SashaChernykh
@REM @Date: 2025-03-15 15:20:41
@REM @Last Modified by: SashaChernykh
@REM @Last Modified time: 2025-03-17 13:55:19


START /B CMD /C pipenv run gh-release-install Kristinita/tidy-html5 tidy.exe .venv/Scripts --verbose

START /B CMD /C pipenv run gh-release-install sharkdp/fd fd-{tag}-x86_64-pc-windows-gnu.zip --extract fd-{tag}-x86_64-pc-windows-gnu/fd.exe .venv/Scripts/fd.exe --verbose
