from flask import Blueprint, request

whois_bp = Blueprint('whois-bp', __name__, url_prefix='/')


@whois_bp.route('/whois', methods=('GET', 'POST'))
def get_whois_data():
    from hyperion_worker.tasks import get_whois_data_async

    domain = request.args.get("domain")
    res = get_whois_data_async.apply_async(args=[domain])
    return res.get()
