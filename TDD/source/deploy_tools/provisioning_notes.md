Provisioning a new site
=======================

## Not sure what (if any of this) applies to my project. Seems to have
## been done already.

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
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
         
         
trying some .htaccess commands to make static work

AddHandler fcgid-script .fcgi
RewriteEngine On
RewriteCond %{REQUEST_URI} !^/static
RewriteCond %{REQUEST_URI} !\.(css|png|jpg|gif)$
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ dispatch.fcgi/$1 [QSA,L]

