#!/usr/bin/env python
"""Custom Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management import execute_from_command_line

def set_db_for_router(db_name):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playground.settings")
    from django.conf import settings
    settings.DATABASES['default'] = settings.DATABASES[db_name]

if __name__ == "__main__":
    # Example usage: python custom_manage.py db_name migrate
    set_db_for_router(sys.argv[1])  # Pass the database name as an argument
    del sys.argv[1]  # Delete the database name argument after the routing
    execute_from_command_line(sys.argv)
