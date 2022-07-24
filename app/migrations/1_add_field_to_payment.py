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
        migrator.add_column('payment', 'is_issued', BooleanField(verbose_name="Error or not", default=False)),
    )
