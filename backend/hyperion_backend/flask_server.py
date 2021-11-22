import os
from flask import Flask, render_template
from . import dns_plugin, whois_plugin


def create_app():
    flask_app = Flask(__name__, template_folder='templates')

    # Get Celery config from environment variables
    flask_app.config.update(
        CELERY_BROKER_URL=os.environ.get('CELERY_BROKER_URL') or 'amqp://guest:guest@localhost:5672',
        CELERY_RESULT_BACKEND=os.environ.get('CELERY_RESULT_BACKEND') or 'rpc://'
    )

    @flask_app.route('/', methods=['GET'])
    def home():
        return render_template('base.html')

    # Register all Flask BluePrints
    flask_app.register_blueprint(dns_plugin.dns_bp)
    flask_app.register_blueprint(whois_plugin.whois_bp)

    return flask_app


flask_app = create_app()
