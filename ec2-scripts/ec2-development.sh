#!/usr/bin/bash

# Install packages
yum -y update
yum install -y tree python3
# amazon-linux-extras install -y java-openjdk11
# yum install -y java-11-openjdk-devel
yum install -y git
amazon-linux-extras install -y nginx1
amazon-linux-extras enable postgresql13
yum clean metadata

yum install -y gcc
yum install -y python3-devel
yum install -y postgresql
yum install -y postgresql-develop

yum -y update

sudo systemctl start nginx


# Configure/install custom software
cd /home/ec2-user
git clone https://github.com/ffukuchi/python-image-gallery.git

chown -R ec2-user:ec2-user python-image-gallery
su ec2-user -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"


# Start/enable services
systemctl stop postfix
systemctl disable postfix

