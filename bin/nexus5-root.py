# -*- coding: utf-8 -*-
# nexus5-root (c) Ian Dennis Miller

from fabric.api import task
# import requests


@task
def download():
    "rsync local changes (ignoring git)"
