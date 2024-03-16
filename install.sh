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

xargs -a manifest cp -R -t $INSTALLDIR

sudo cp hashcodes.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable hashcodes
sudo systemctl restart hashcodes
