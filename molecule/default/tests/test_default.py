import os
import pytest
import docker
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


""" helper functions"""


def get_docker_image_name():
    client = docker.from_env()
    test_container = client.containers.list()[0]
    return test_container.attrs['Config']['Image']


def check_file(filepath, user, group, permission):
    assert filepath.exists
    assert filepath.user == user
    assert filepath.group == group
    assert oct(filepath.mode) == permission


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


""" tasks/main.yml tests """


@pytest.mark.parametrize('files', [
    '/etc/acro/add-website.conf'
])
def test_file_paths(host, files):
    test_files = [files]
    [check_file(host.file(x), 'root', 'root', '0o777') for x in test_files]

    # Validate /etc/acro/add-website.conf.php{{version}}
    php_version = get_docker_image_name()[-2:]
    php_version = '.php' + php_version[0] + '.' + php_version[1]
    file_name = host.file(test_files[0] + php_version)
    check_file(file_name, 'root', 'root', '0o644')


def test_host_system(host):
    assert host.system_info.distribution == 'ubuntu'
