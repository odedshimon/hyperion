from flask_cors import CORS

from .flask_server import flask_app

if __name__ == "__main__":
    # enable CORS
    CORS(flask_app, resources={r'/*': {'origins': '*'}})
    flask_app.run()


