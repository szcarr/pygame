#!/bin/bash
PROJECTDIR="$(pwd)/"
CONFIGDIR="${PROJECTDIR}src/cfg/"

$MSG="STUPID STARTING FILES."
# DELETING PERSONAL FILES
for file in $PROJECTDIR*
do
    #echo $file
    if [ "${file}" = "${PROJECTDIR}TextUIstart.sh" ]
    then
        echo $MSG
        rm -rf TextUIstart.sh
    elif [ "${file}" = "${PROJECTDIR}TextUIstart.bat" ]
    then
        echo $MSG
        rm -rf TextUIstart.bat
    fi
done

rm -rf $CONFIGDIR


# FINDING AND DELETING ALL PYCACHES
pycache="$(find * | grep '__pycache__')"

for f in $pycache
do
    file="${PROJECTDIR}${f}"
    if [ -d "$file" ] # Check if folder exists
    then
        #rm -rf
        echo "Found stupid sinner."
        echo $file  
        rm -rf $file
    fi
done

# ADDING TO GITHUB

git init .
git commit -m "Python version"
git remote add "Pygame" https://github.com/szcarr/pygame.git
git add *
git push pygame main