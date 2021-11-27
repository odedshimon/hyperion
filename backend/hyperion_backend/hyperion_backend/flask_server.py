import os
from flask import Flask, render_template

from hyperion_blueprints import dns_bp, whois_bp


def create_app():
    app = Flask(__name__, template_folder='templates')

    # Get Celery config from environment variables
    app.config.update(
        CELERY_BROKER_URL=os.environ.get('CELERY_BROKER_URL') or 'amqp://guest:guest@localhost:5672',
        CELERY_RESULT_BACKEND=os.environ.get('CELERY_RESULT_BACKEND') or 'rpc://'
    )

    @app.route('/', methods=['GET'])
    def home():
        return render_template('base.html')

    # Register all Flask BluePrints
    app.register_blueprint(dns_bp)
    app.register_blueprint(whois_bp)

    return app


flask_app = create_app()
