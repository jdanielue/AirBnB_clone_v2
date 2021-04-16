#!/usr/bin/env bash
# prepare your web servers

if ! [ -x "$(command -v nginx)" ]; then
    apt update -y;
    apt install nginx -y;
fi

service nginx start

if [ ! -d /data/ ]; then
  mkdir /data/;
fi

if [ ! -d /data/web_static/ ]; then
  mkdir /data/web_static/;
fi

if [ ! -d /data/web_static/releases/ ]; then
  mkdir /data/web_static/releases/;
fi

if [ ! -d /data/web_static/shared/ ]; then
  mkdir /data/web_static/shared/;
fi

if [ ! -d /data/web_static/releases/test/ ]; then
  mkdir /data/web_static/releases/test/;
fi

if [ ! -d /data/web_static/releases/test/index.html ]; then
  touch /data/web_static/releases/test/index.html;
  echo Holberton Scholli | tee /data/web_static/releases/test/index.html
fi

if [ ! -d /data/web_static/current ]; then
  ln -s /data/web_static/releases/test /data/web_static/current;
else
  rm /data/web_static/current;
  ln -s /data/web_static/releases/test /data/web_static/current;
fi
sudo chown -R ubuntu:ubuntu /data/

sed -i '/listen 80 default_server;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default

service nginx restart
