#!/bin/bash
cd /home/ec2-user/cn-django-test
sudo docker-compose down
sudo docker-compose up -d --build
