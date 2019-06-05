
# django-linux-users-control-panel 

This is an use case of django, python and sqlite to build a basic tool to manage linux groups and users.
The scripts to manage Linux users and groups must be developed by you. This example provides a suggested class in osprocess.py to interact with Linux commands, osprocess class uses the super command for a more secure implementation.

Requirements:
 * Django (v2.2.1)
 * python (v3.5)
 * sqlite (v3)

How to Install

 * Download and unzip the project source code
 * Get into decompressed code directory and execute following commands:
```
# python3 manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK

# python3 manage.py makemigrations Admin_Users_Groups

Migrations for 'Admin_Users_Groups':
  Admin_Users_Groups/migrations/0001_initial.py
    - Create model User
    - Create model Group

# python3 manage.py migrate

Operations to perform:
  Apply all migrations: Admin_Users_Groups, admin, auth, contenttypes, sessions
Running migrations:
  Applying Admin_Users_Groups.0001_initial... OK

# python3 manage.py createsuperuser

# python3 manage.py runserver
```
 * Open url http://localhost:8000/admin
 * Then login with superuser
 * In first section called "AUTHENTICATION AND AUTHORIZATION", you can to manage django platform users and groups 
 * In secong section called "SERVER USERS AND GROUPS", you manage users, groups a their relations impacting to linux user and groups.
 * RECOMENDATION: to be used in production environments I suggest the use of https protocol.
