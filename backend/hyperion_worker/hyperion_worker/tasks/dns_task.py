import dns.resolver
from .. import celery_app

DNS_QUERY_TYPES = ['NS', 'MX', 'SOA', 'A', 'CNAME', 'AAAA']


@celery_app.task
def get_dns_data_async(domain):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8']

    res = {}
    for qtype in DNS_QUERY_TYPES:
        try:
            answers = resolver.resolve(domain, qtype)
            res[qtype] = [str(a) for a in answers]
        except dns.resolver.NoAnswer as e:
            print(f"No DNS records of type {qtype} for {domain}")
        except Exception as e:
            print(f"Failed to fetch DNS data for {domain}: {e}")
            break

    return res
