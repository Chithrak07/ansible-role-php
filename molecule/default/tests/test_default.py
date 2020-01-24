import os
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


""" helper functions"""


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
def test_file_paths_ubuntu1804(host, files):
    if host.system_info.release == '18.04' \
            and host.system_info.distribution == 'Ubuntu':
        test_files = [files]
        [check_file(host.file(x), 'root', 'root', '0o644') for x in test_files]
