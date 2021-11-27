from flask import Blueprint, request


dns_bp = Blueprint('dns', __name__, url_prefix='/')


@dns_bp.route('/dns', methods=('GET', 'POST'))
def get_dns_data():
    from hyperion_worker.tasks import get_dns_data_async
    domain = request.args.get("domain")
    res = get_dns_data_async.apply_async(args=[domain])
    return res.get()
