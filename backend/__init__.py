from flask import Flask, render_template
from flask_cors import CORS


def create_app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/', methods=['GET'])
    def home():
        return render_template('base.html')

    # Register all Flask BluePrints
    from backend import dns_plugin, whois_plugin
    app.register_blueprint(dns_plugin.dns_bp)
    app.register_blueprint(whois_plugin.whois_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.run()
