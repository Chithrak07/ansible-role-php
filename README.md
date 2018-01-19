php
======

For setting up PHP on an Ubuntu 14.04 or 16.04 server.


Requirements
------------
* Ubuntu 14.04 or 16.04

Role Variables
--------------
php_default_version: The default version of php for the server
php_memory_limit: The maximum memory limit
php_max_input_vars: The maximum input vars
php_versions: A list of versions to install

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: acromedia.php }

License
-------

BSD

Author Information
------------------

Acro Media Inc.
https://www.acromedia.com/
