Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, crimson.rocks

## Upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, crimson.rocks

## Folder structure:
Assume we have a user account at /home/username

/home/username
    sites
        SITENAME
            database
            source
            virtualenv
            static

## Some tips (BUG: also need to substitute username!)

sed "s/SITENAME/ACTUAL_NAME/g" \
    deploy_tools/nginx.template.conf | sudo tee \
    /etc/nginx/sites-available/ACTUAL_NAME

ln -s ../sites-available/ACTUAL_NAME \
    /etc/nginx/sites-enables/ACTUAL_NAME

sed "s/SITENAME/ACTUAL_NAME/g" \
    deploy_tools/gunicorn-upstart.template.conf | sudo tee \
    /etc/init/gunicorn-ACTUAL_NAME.conf

service nginx reload
start gunicorn-ACTUAL_NAME