from django.core.management.base import BaseCommand, CommandError
import os

DB_CONTAINER = 'pg_db'
DB_USER = 'postgres'
DB_NAME = 'imdb'


class Command(BaseCommand):
    help = 'Fill the database with data from .csv files'

    def add_arguments(self, parser):
        """Add requirement argument path which is the path to the sql script to fill the db"""
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        """Fill the database inside pg_db container"""
        try:
            os.system(
                f'docker exec -u {DB_USER} {DB_CONTAINER} psql {DB_NAME} {DB_USER} -f {options["path"]}')
        except:
            raise CommandError('Could not execute the command')
