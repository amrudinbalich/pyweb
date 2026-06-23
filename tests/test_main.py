from main import application

def call_app(path="/", method="GET"):
    captured = {}

    def start_response(status, headers):
        captured["status"] = status

    environ = {"PATH_INFO": path, "REQUEST_METHOD": method, "QUERY_STRING": ""}
    body = b"".join(application(environ, start_response))
    return captured["status"], body


def test_home_page():
    status, body = call_app("/")
    print(status, body)
    assert status == "200 OK"