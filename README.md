# Ansible role: PHP

Install and configure PHP for use with Drupal sites in Acro hosting environments (NGINX + FPM).

## Requirements

* Ubuntu LTS (14.04 or newer)

## Role Variables

* php_default_version: The default CLI version of php for the server
* php_memory_limit: The maximum memory limit
* php_max_input_vars: The maximum input vars
* php_versions: A list of versions to install
* phpXX_add_modules: A list of extra apt packages not already included in the [default list](./defaults/main.yml), where XX corresponds to the PHP version(s) you're installing.

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
      php71_add_modules:
        - php7.1-extra-thingy
      tags:
        - php

## License

GPLv3

## Author Information

Acro Media Inc.
https://www.acromedia.com/
