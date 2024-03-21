#!/bin/bash
INSTALLDIR=/home/ubuntu/hashcodes

sudo apt install python3-venv

python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt
deactivate

mkdir $INSTALLDIR 2> /dev/null
sudo chgrp www-data $INSTALLDIR

sudo cp hashcodes.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable hashcodes

# Need to stop execution because otherwise won't be able to copy uwsgi binary
sudo systemctl stop hashcodes
xargs -a manifest cp -R -t $INSTALLDIR

sudo systemctl start hashcodes

# After using certbot this update isn't going to work. The two lines below should be done 
# before running the certbot command
# sudo cp hashcodes.k2dbk.com /etc/nginx/sites-available
# sudo ln -s /etc/nginx/sites-available/hashcodes.k2dbk.com /etc/nginx/sites-enabled

sudo systemctl reload nginx