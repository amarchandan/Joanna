# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'LAMO'


# if __name__ == "__main__":
#     app.run()

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
