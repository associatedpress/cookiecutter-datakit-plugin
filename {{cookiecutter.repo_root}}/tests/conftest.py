import os
import shutil

import pytest
from datakit.utils import makedirs, mkdir_p, write_json


@pytest.fixture
def cookiecutter_home(tmpdir):
    return os.path.join(str(tmpdir), '.cookiecutters')


@pytest.fixture
def datakit_home(tmpdir):
    return os.path.join(str(tmpdir), '.datakit')


@pytest.fixture
def plugin_dir(datakit_home):
    return os.path.join(datakit_home, 'plugins/{{ cookiecutter.repo_root }}')


@pytest.fixture
def create_plugin_config_default(plugin_dir):
    config_file = os.path.join(plugin_dir, 'config.json')
    config = {'default_template': ''}
    write_json(config_file, config)


@pytest.fixture
def deploy_template():
    copied_repos = []
    def _deploy_template(cc_home, repo_path):
        src_repo = repo_path
        base_name = repo_path.split('/')[-1]
        dest_repo = os.path.join(cc_home, base_name)
        shutil.copytree(src_repo, dest_repo)
        copied_repos.append(dest_repo)
        return dest_repo

    yield _deploy_template

    for repo in copied_repos:
        shutil.rmtree(repo)


@pytest.fixture(autouse='session')
def setup_environment(monkeypatch, datakit_home):
    mkdir_p(datakit_home)
    monkeypatch.setenv('DATAKIT_HOME', datakit_home)

@pytest.fixture(autouse="module")
def create_plugin_dir(plugin_dir):
    mkdir_p(plugin_dir)
    yield
    shutil.rmtree(plugin_dir)
