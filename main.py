# mental map
# request -> nginx
# gunicorn - wsgi
# app code
# gunicorn - api

# WSGI interface contract
def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')

    if path == '/':
        body = b'Hello from home page!'
        status = '200 OK'
    elif path == '/about':
        body = b'About page'
        status = '200 OK'
    else:
        body = b'404 Not Found'
        status = '404 Not Found'

    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, headers)
    return [body]