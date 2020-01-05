#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local, env, put, run
from datetime import datetime
import os
env.hosts = ['35.196.153.56', '34.73.85.88']
env.user = "ubuntu"


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
        try:
            path = archive_path.split('/')[1]
            no_ext = path.split('.')[0]
            data = "/data/web_static/releases/" + no_ext + "/"
            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(data))
            run("tar -xzf /tmp/{} -C {}".format(path, data))
            run("rm /tmp/{}".format(path))
            run("mv {}web_static/* {}".format(data, data))
            run("rm -rf {}web_static".format(data))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(data))
            return True
        except Exception:
            return False
    else:
        return False
