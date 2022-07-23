from playhouse.migrate import *
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from dependencies import get_db


db = get_db()
migrator = PostgresqlMigrator(db)

if __name__ == "__main__":
    migrate(
        migrator.alter_column_type('payment', 'status', CharField()),
    )
