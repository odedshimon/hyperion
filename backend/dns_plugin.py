import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query
import dns.resolver
from flask import Blueprint, request

DNS_QUERY_TYPES = ['NS', 'MX']

dns_bp = Blueprint('dns', __name__, url_prefix='/')


@dns_bp.route('/dns', methods=('GET', 'POST'))
def get_dns_data():
    domain = request.args.get("domain")
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8']

    res = {}
    for qtype in DNS_QUERY_TYPES:
        answers = resolver.resolve(domain, qtype)
        res[qtype] = [str(a) for a in answers]

    return res
