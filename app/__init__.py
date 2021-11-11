from flask import Flask, render_template
from flask_cors import CORS


def create_app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/', methods=['GET'])
    def home():
        return render_template('base.html')

    # Register all Flask BluePrints
    from app import dns
    app.register_blueprint(dns.dns_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.run()
