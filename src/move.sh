#Ikkje tenk paa denne
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..
cd ..

#ssh-keygen
#ssh-copy-id -i ~/.ssh/id_rsa pi@192.168.1.170

#USER="isak"
#IP="192.168.1.131"

USER="isak"
IP="192.168.1.131"
FILE="pygame"

rm -rf $FILE.zip
zip -r $FILE.zip $FILE
scp $FILE.zip $USER@$IP:/home/$USER/
rm -rf $FILE.zip