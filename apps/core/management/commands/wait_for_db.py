import time

from django.core.management.base import BaseCommand
from django.db import OperationalError, connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('wait for db...')
        db_con = False
        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Database unavailable, wait 1 second')
                time.sleep(1)
        self.stdout.write('Database available!!!')