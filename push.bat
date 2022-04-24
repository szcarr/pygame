REM Use this batch file to push this folder to github
REM Place in folder you want to upload
REM Replace origin link to your own repository
git init
git add .
git commit -m "New version"
git remote rm origin
git remote add origin https://github.com/szcarr/TextUI.git
REM git pull --rebase origin master
git push -f origin master
REM pause