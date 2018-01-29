from flask import Flask
from web.ui import cpk
from config import app_details


# app = Flask(__name__)
# app.register_blueprint(cpk, url_prefix=app_details['path'])
# app.register_blueprint(cpk)


if __name__ == '__main__':
    cpk.run(
        host=app_details['host'],
        port=app_details['port'],
        debug=True
    )
