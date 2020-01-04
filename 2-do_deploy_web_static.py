#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from fabric.operations import *
from datetime import datetime
import os


def do_pack():
    """create a tgz archive from contents of web_static folder"""
    try:
        local("mkdir -p versions")
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            time))
        return "versions/web_static_{}.tgz".format(time)
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if (os.path.exists(archive_path)):
        path = archive_path.split('/')[1]
        return True
    else:
        return False
