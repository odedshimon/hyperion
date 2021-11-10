from flask import Flask, render_template


def create_app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/')
    def home():
        return render_template('base.html')

    from app import dns
    app.register_blueprint(dns.dns_bp)

    return app


if __name__ == "__main__":
    create_app().run()
