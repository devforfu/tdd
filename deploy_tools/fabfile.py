from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random


REPO_URL = "https://github.com/devforfu/tdd.git"


__all__ = ["deploy"]


def deploy():
    """
    Entry point for Fabric deployment process.
    """
    site_folder = "/home/{}/sites/{}".format(env.user, env.host)
    source_folder = site_folder + "/source"
    create_directory_structure_if_necessary(site_folder)
    get_latest_source(source_folder)
    update_settings(source_folder, env.host)
    update_virtualenv(source_folder)
    update_static_files(source_folder)
    update_database(source_folder)


def create_directory_structure_if_necessary(site_folder):
    """
    Creates project structure specified in provisioning notes.
    """
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run("mkdir -p {}/{}".format(site_folder, subfolder))


def get_latest_source(source_folder):
    if exists(source_folder + "/.git"):
        run("cd {} && git fetch".format(source_folder))
    else:
        run("git clone {} {}".format(REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run("cd {} && git reset --hard {}".format(source_folder, current_commit))


def update_settings(source_folder, site_name):
    """
    Makes appropriate changes to settings.py to make it ready for deployment.
    """
    settings_path = source_folder + "/superlists/settings.py"
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',
        'ALLOWED_HOSTS = ["{}"]'.format(site_name))
    secret_key_file = source_folder + "/superlists/secret_key.py"
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '{}'".format(key))
    append(settings_path, "\nfrom .secret_key import SECRET_KEY")


def update_virtualenv(source_folder):
    virtualenv_folder = source_folder + "/../virtualenv"
    if not exists(virtualenv_folder + "/bin/pip"):
        run("virtualenv --python=python3 {}".format(virtualenv_folder))
    run("{}/bin/pip install -r {}/requirements.txt".format(
        virtualenv_folder, source_folder
    ))


def update_static_files(source_folder):
    run("cd {} && ../virtualenv/bin/python3 manage.py collectstatic --noinput"
        .format(source_folder))


def update_database(source_folder):
    run("cd {} && ../virtualenv/bin/python3 manage.py migrate --noinput"
        .format(source_folder))
