# app/management/commands/renameproject.py

import os
import glob
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Renames the Project'

    def add_arguments(self, parser):
        parser.add_argument('old', nargs='+', type=str, help="current project name")
        parser.add_argument('new', nargs='+', type=str, help="new project name")

    def handle(self, *args, **options):
        old = options["old"][0]
        new = options["new"][0]

        base = str(settings.BASE_DIR)
        projectfiles = []
        managefile = os.path.join(base, "manage.py")
        projectfiles.append(managefile)
        projectfiles += glob.glob(os.path.join(base, old, "*.py"))
        projectfiles += glob.glob(os.path.join(base, old, "**", "*.py"))
        for pythonfile in projectfiles:
            with open(pythonfile, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(old, new)

            with open(pythonfile, 'w') as file:
                file.write(filedata)
        os.rename(os.path.join(base, old), os.path.join(base, new))