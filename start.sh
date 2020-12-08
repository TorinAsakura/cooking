#!/bin/sh
python manage.py runfcgi --settings=povary.settings maxchildren=10 maxspare=1 minspare=1 method=prefork socket=/home/scarface/www/povary.ru/povary/log/django.sock pidfile=/home/scarface/www/povary.ru/povary/log/django.pid
