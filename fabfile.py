# coding=utf-8
import os

from fabric.api import env
from fabric.context_managers import cd
from fabric.decorators import roles
from fabric.operations import run

env.roledefs['production'] = ['django@production.server.ip:port']


def production_env():
    """Production environment"""

    # Speedup connection setup to server.
    env.disable_known_hosts = True

    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')]
    env.user = 'django'
    env.project_root = '/home/{{ project_name }}/{{ project_name }}/'
    env.shell = '/bin/bash -c'

    # I usually place virtualenv into BASE_DIR/env folder. You can do same or use your paths.
    env.virtenv = '%s/env' % env.project_root
    env.python = '%s/bin/python' % env.virtenv
    env.pip = '%s/bin/pip' % env.virtenv


@roles('production')
def deploy():
    git_pull()
    pip_install()
    collectstatic()
    # static_compress()


@roles('production')
def git_pull():
    production_env()
    with cd(env.project_root):
        run('git pull origin master')


@roles('production')
def collectstatic():
    production_env()
    with cd(env.project_root):
        run('docker-compose run assets-prod')

        run('{0} manage.py collectstatic --noinput'.format(env.python))


@roles('production')
def static_compress():
    production_env()
    with cd(env.project_root):
        run('{0} manage.py compress'.format(env.python))


@roles('production')
def pip_upgrade():
    production_env()
    run('{pip} install -U -r {filepath}'.format(pip=env.pip,
                                                filepath=os.path.join(env.project_root, 'requirements.txt')))


@roles('production')
def pip_install():
    production_env()
    run('{pip} install -q -r {filepath}'.format(pip=env.pip,
                                                filepath=os.path.join(env.project_root, 'requirements.txt')))


@roles('production')
def migrate():
    production_env()
    with cd(env.project_root):
        run('{0} manage.py migrate'.format(env.python))


@roles('production')
def syncdb():
    production_env()
    with cd(env.project_root):
        run('{0} manage.py syncdb'.format(env.python))


@roles('production')
def update():
    deploy()
    migrate()
    reload_all()


@roles('production')
def clear_cache():
    production_env()
    with cd(env.project_root):
        run('{0} manage.py clear_cache'.format(env.python))


@roles('production')
def reload_all():
    production_env()
    run('supervisorctl restart {{ project_name }}:')
