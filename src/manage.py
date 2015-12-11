#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print "server is started now"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restapi.settings")

    from django.core.management import execute_from_command_line

    print "Going to execute command"
    for i in sys.argv:
      print i

    execute_from_command_line(sys.argv)
