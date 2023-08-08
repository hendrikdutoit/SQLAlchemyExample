REM CLS
@ECHO ON
IF /I "%2"=="ON" (
    set _debug=ON
    ) ELSE (
    set _debug=OFF
)
IF %1=="" GOTO :AppHelp

@ECHO %_debug%
ECHO Push current branch to GitHub
ECHO '
CALL del_dt.bat
rstcheck README.rst
gitit adda
gitit commitcust -m %1
gitit pushall
GOTO :Exit

:AppHelp
@ECHO usage: push message debug
@ECHO where
@ECHO  - message: Description of the changes
@ECHO  - debug:   ON or OFF
@ECHO eg. push "Updated foo.bat"
ECHO '
GOTO :Exit

:Exit
EXIT /B 0
