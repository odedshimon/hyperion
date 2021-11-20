import dns.resolver
from flask import Blueprint, request

DNS_QUERY_TYPES = ['NS', 'MX', 'SOA', 'A', 'CNAME', 'AAAA']

dns_bp = Blueprint('dns', __name__, url_prefix='/')


@dns_bp.route('/dns', methods=('GET', 'POST'))
def get_dns_data():
    domain = request.args.get("domain")
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8']

    res = {}
    for qtype in DNS_QUERY_TYPES:
        try:
            answers = resolver.resolve(domain, qtype)
            res[qtype] = [str(a) for a in answers]
        except dns.resolver.NoAnswer as e:
            print(f"No DNS records of type {qtype} for {domain}")

    return res
