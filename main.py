# mental map
# request -> nginx ->
# -> gunicorn (input) -> app code (custom/django/flask) -> gunicorn (output)

# note: Gunicorn is built on top of WSGI definition

from pathlib import Path
from services.database import database_connect
from services.helpers import json_serializer
from mysql.connector.connection import MySQLConnection

import json

BASE_DIR = Path(__file__).resolve().parent

def read_view(name):
    return (BASE_DIR / "resources" / "views" / name).read_bytes()

def get_users(database: MySQLConnection):
    cursor = database.cursor(dictionary=True)

    try:
        q = 'SELECT * FROM users'
        cursor.execute(q)
        return cursor.fetchall()
    finally:
        cursor.close()


# WSGI interface contract - Gunicorn calls it -> boot the app code
def application(environ, start_response):
    database = None

    try:
        database = database_connect()

        path = environ.get('PATH_INFO', '/')
        request_method = environ['REQUEST_METHOD']

        status = '200 OK'
        content_type = 'text/html'

        if path == '/' and request_method == 'GET':
            body = read_view('index.html')

        elif path == '/about':
            body = b'About page'

        elif path == '/users':
            users = get_users(database)

            # from pprint import pprint
            # pprint(users)

            body = json.dumps(
                users,
                default=json_serializer
            ).encode("utf-8")
            content_type = 'application/json'

        else:
            body = b'404 Not Found'
            status = '404 Not Found'
            content_type = 'text/plain'

        headers = [
            ('Content-Type', content_type),
            ('Content-Length', str(len(body)))
        ]

        start_response(status, headers)
        return [body]

    except Exception as e:
        import traceback
        print(traceback.format_exc())

        start_response(
            '500 Internal Server Error',
            [('Content-Type', 'text/plain')]
        )
        return [str(e).encode()]

    finally:
        if database:
            database.close()