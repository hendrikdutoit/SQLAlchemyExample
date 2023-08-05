REM CLS
@ECHO OFF
IF /I "%2"=="ON" (
    set _debug=ON
    ) ELSE (
    set _debug=OFF
)
IF "%1"=="" GOTO :AppHelp

@ECHO %_debug%
ECHO Push a new release (%1) to GitHub
ECHO '

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "Hr=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

CALL del_dt.bat
git commit --allow-empty -m "Release %1"
git tag -a %1-%YY%%MM%%DD%%Hr%%Min%%Sec% -m "Version %1"
git push --tags
git checkout master
git branch --all
GOTO :Exit

:AppHelp
@ECHO usage: release version
@ECHO where
@ECHO  - version: MAJOR.MINOR.PATCH
@ECHO      MAJOR version when you make incompatible API changes
@ECHO      MINOR version when you add functionality in a backward compatible manner
@ECHO      PATCH version when you make backward compatible bug fixes
@ECHO eg. release 1.2.3
@ECHO see www.semver.org
GOTO :Exit

:Exit
EXIT /B 0
