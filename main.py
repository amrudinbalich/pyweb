# mental map
# request -> nginx ->
# -> gunicorn (input) -> app code (custom/django/flask) -> gunicorn (output)

# note: Gunicorn is built on top of WSGI definition

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def read_view(name):
    return (BASE_DIR / "resources" / "views" / name).read_bytes()


# WSGI interface contract - Gunicorn calls it -> boot the app code
def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    request_method = environ['REQUEST_METHOD']

    content_type = 'text/html'

    if path == '/' and request_method == 'GET':
        body = read_view('index.html')
        status = '200 OK'
        content_type = 'text/html'
    elif path == '/about':
        body = b'About page'
        status = '200 OK'
    else:
        body = b'404 Not Found'
        status = '404 Not Found'

    headers = [
        ('Content-Type', content_type or 'text/html'), # -->> default
        ('Content-Length', str( len(body) ))
    ]
    start_response(status, headers)
    return [body]