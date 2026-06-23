from mysql.connector.aio.cursor import MySQLCursor

from services.database import database_connect
from services.helpers import root_dir, this_time
from pathlib import Path
from pprint import pp


MIGRATIONS_DIR = Path(f'{root_dir()}/migrations')


def table_exists(cursor: MySQLCursor, table_name) -> bool:
    cursor.execute(f'SHOW TABLES LIKE {table_name}')
    table = cursor.fetchone()

    return table is not None


def run_migrations() -> int:
    conn = database_connect()
    cursor = conn.cursor()

    for file in sorted( MIGRATIONS_DIR.glob('*.sql') ):
        print(f'Migrating: {file.name} ...')

        sql = file.read_text()
        cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()

    return 1

if __name__ == '__main__':
    if run_migrations():
        print(f'finished ({this_time()})')