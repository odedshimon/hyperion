import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query
from flask import Blueprint, request

dns_bp = Blueprint('dns', __name__, url_prefix='/')


@dns_bp.route('/dns', methods=('GET', 'POST'))
def get_dns_data():
    domain = request.args.get("domain")
    target_name = dns.name.from_text(domain)
    q = dns.message.make_query(target_name, dns.rdatatype.NS)
    r = dns.query.udp(q, '8.8.8.8')
    ns_rrset = r.find_rrset(r.answer, target_name, dns.rdataclass.IN, dns.rdatatype.NS)

    res = {}
    res["NS"] = [str(rr) for rr in ns_rrset]

    return res
