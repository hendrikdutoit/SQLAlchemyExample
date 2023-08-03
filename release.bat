CALL del_dt.bat
CALL git commit --allow-empty -m "Release %1"
CALL git tag -a %1.%2 -m "Version %1"
CALL git push --tags
CALL git checkout master
CALL git branch
