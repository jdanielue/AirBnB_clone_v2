#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """script that generates a .tgz archive"""
    try:
        now = datetime.now()
        local('mkdir -p versions/')
        dt_string = now.strftime("%Y%m%d%H%M%S")
        filename = "web_static_" + dt_string + ".tgz"
        local('tar -cvzf versions/{} web_static/'.format(filename))
        path = './versions/{}'.format(filename)
        print("web_static packed: {} ->{}Bytes"
              .format(path, os.path.getsize(path)))
    except:
        return None
if __name__ == "__main__":
    do_pack()
