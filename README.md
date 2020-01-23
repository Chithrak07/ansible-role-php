# Ansible role: PHP

Install and configure PHP for use with Drupal sites in Acro hosting environments (NGINX + FPM).

# Test Suite Setup (Molecule)

- To run the whole test suite for all environments
```bash
$ tox
```

## Setup Local Virtual Environment

- to run a single test
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install 'molecule[docker]'
$ pip3 install -r requirements.txt
$ MOLECULE_DISTRO=ubuntu1804-php71 molecule test
```

- note that you can substitute MOLECULE_DISTRO=version for the following:

__MOLECULE_DISTRO List__
    
    ubuntu1804-php72
    ubuntu1804-php71
    ubuntu1804-php70
    
    ubuntu1604-php72
    ubuntu1604-php71
    ubuntu1604-php70

- look here for more images: https://hub.docker.com/r/geerlingguy/
    
### Development

- if you are creating a new molecule test suite inside an existing role then execute this ...
```bash 
$ molecule init scenario -r ansible-role-php
```
- you can change one line and enter a different molecule command to keep the container alive
    - from the ```MOLECULE_DISTRO``` list above, substitute your desired version for development below
    
```bash
    /molecule/molecule.yml
    image: "superelectron/docker-ubuntu-ansible-php:${MOLECULE_DISTRO:-ubuntu1804-php72}"
```

- run this command so that the container is not dead
```bash
$ molecule test --destroy=never
```

- ssh into the container after the test
```bash
$ molecule login
```

- run the test suite located in ```molecule/test/test_default.py```
```bash
$ molecule verify
```

## Requirements

* Ubuntu LTS (14.04 or newer)

## Role Variables

* php_default_version: The default CLI version of php for the server
* php_memory_limit: The maximum memory limit
* php_max_input_vars: The maximum input vars
* php_versions: A list of versions to install

## Dependencies

None

## Example Playbook

    - hosts: servers
    - name: Install + Configure PHP
      role: acromedia.php
      php_default_version: 7.1
      php_versions:
        - 5.6
        - 7.0
        - 7.1
        - 7.2
      tags:
        - php

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/
