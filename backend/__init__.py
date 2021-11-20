import os

from celery import Celery
from flask import Flask, render_template
from flask_cors import CORS


def create_app():
    flask_app = Flask(__name__, template_folder='templates')

    # Get Celery config from environment variables
    flask_app.config.update(
        CELERY_BROKER_URL=os.environ.get('CELERY_BROKER_URL') or 'amqp://localhost:5672',
        CELERY_RESULT_BACKEND=os.environ.get('CELERY_RESULT_BACKEND') or 'rpc://'
    )

    @flask_app.route('/', methods=['GET'])
    def home():
        return render_template('base.html')

    # Register all Flask BluePrints
    from backend import dns_plugin, whois_plugin
    flask_app.register_blueprint(dns_plugin.dns_bp)
    flask_app.register_blueprint(whois_plugin.whois_bp)

    return flask_app


def make_celery(flask_app):
    celery_app = Celery(
        flask_app.import_name,
        backend=flask_app.config['CELERY_RESULT_BACKEND'],
        broker=flask_app.config['CELERY_BROKER_URL']
    )
    celery_app.conf.update(flask_app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


if __name__ == "__main__":
    app = create_app()
    celery = make_celery(app)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.run()
