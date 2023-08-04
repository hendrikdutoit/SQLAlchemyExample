for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "Hr=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

CALL del_dt.bat
CALL git commit --allow-empty -m "Release %1"
CALL git tag -a %1.%YY%%MM%%DD%%HH%%Min%%Sec% -m "Version %1"
CALL git push --tags
CALL git checkout master
git branch
