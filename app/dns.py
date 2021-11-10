from flask import Blueprint

dns_bp = Blueprint('dns', __name__, url_prefix='/')


@dns_bp.route('/dns', methods=('GET', 'POST'))
def get_dns_data():
    return "dns"
