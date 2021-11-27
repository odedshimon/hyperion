import whois
from .. import celery_app


@celery_app.task
def get_whois_data_async(domain):
    return whois.whois(domain)
