# coding=utf-8
import os

from fabric.api import env


env.roledefs['production'] = ['django@production.server.ip:port']


def production_env():
    """Production environment"""
    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')]
    env.user = 'django'
    env.project_root = 'path to project base dir'
    env.shell = '/bin/bash -c'

    # I usually place virtualenv into BASE_DIR/env folder. You can do same or use your paths.
    env.virtenv = '%s/env' % env.project_root
    env.python = '%s/bin/python' % env.virtenv
    env.pip = '%s/bin/pip' % env.virtenv