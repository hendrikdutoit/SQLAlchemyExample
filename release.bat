for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "Hr=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

del_dt.bat
git commit --allow-empty -m "Release %1"
git tag -a %1-%YY%%MM%%DD%%Hr%%Min%%Sec% -m "Version %1"
git push --tags
git checkout master
git branch -all
