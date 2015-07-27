from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/bobm123/DjangoTutorials.git'


def deploy():
    work_folder = '/home/%s/work' % env.user
    site_url = 'balsachips.net'
    site_area = 'balsachips-staging'
    #site_area = 'balsachips-live'
   
    #site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    site_folder = '/home/%s/sites/%s' % (env.user, site_area)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(work_folder)
    _update_settings(work_folder, site_url)
    #if not exists(source_folder):
    #    run('ln -s %s/TDD/source %s' % (work_folder, site_folder))
    run('cp -r %s/TDD/source %s' % (work_folder, site_folder))
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    proj_folders = ('database', 'static', 'virtualenv', 'source')
    #proj_folders = ('database', 'static', 'virtualenv') # remove source because we gonna link to it
    for pf in proj_folders:
        run('mkdir -p %s/%s' % (site_folder, pf))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _update_settings(source_folder, site_name=env.host):
    superlists_path = source_folder + '/TDD/source/superlists'
    settings_path = superlists_path + '/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False") 
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = superlists_path + '/secret_key.py'
    if not exists(secret_key_file): 
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(source_folder):
    #virtualenv_folder = source_folder + '/../virtualenv'
    virtualenv_folder = '/home/ubuntu/sites/balsachips-staging/virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (
            virtualenv_folder, source_folder
    ))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % (
        source_folder,
    ))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % (
        source_folder,
    ))

