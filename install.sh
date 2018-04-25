#!/bin/bash

sudo apt update
sudo apt --assume-yes install python3-guestfs
sudo apt --assume-yes install python3-hivex
sudo apt --assume-yes install python3-pip
pip3 install vminspect

pip3 install celery

sudo apt-get --assume-yes install nfs-common
