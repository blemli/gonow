set -e
name=$(basename $(git rev-parse --show-toplevel))


echo "~~~ install $name admin service ~~~~"
sudo cp -f setup/$name-admin.service /lib/systemd/system/$name-admin.service
sudo chmod 644 /lib/systemd/system/$name-admin.service
sudo systemctl daemon-reload
sudo systemctl enable $name-admin.service
sudo service $name-admin start

