from flask import Blueprint, request

whois_bp = Blueprint('whois-bp', __name__, url_prefix='/')


@whois_bp.route('/whois', methods=('GET', 'POST'))
def get_whois_data():
    import whois
    domain = request.args.get("domain")
    return whois.whois(domain)