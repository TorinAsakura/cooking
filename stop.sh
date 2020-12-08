#!/bin/bash
pid_file=/home/scarface/www/povary.ru/povary/log/django.pid
if [ -a $pid_file ]; then
        pid=`cat $pid_file`
        ps aux | grep -v grep | grep $pid
        if [ $? -eq 1 ]; then
                echo "Could not be stopped."
                echo "There is no process with pid=$pid"
        else
                kill -9 $pid
        fi
fi