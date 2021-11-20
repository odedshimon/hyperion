# To run this celery worker from shell type: celery -A celery_worker.celery_app worker --loglevel=info

from celery import Celery

try:
    from backend.flask_server import flask_app
except:
    # TODO: just a workaround, solve this import while using the celery command from shell
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from backend.flask_server import flask_app


def make_celery(flask_app):
    celery_app = Celery(
        flask_app.import_name,
        backend=flask_app.config['CELERY_RESULT_BACKEND'],
        broker=flask_app.config['CELERY_BROKER_URL']
    )

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


celery_app = make_celery(flask_app)


@celery_app.task()
def get_whois_data_async(domain):
    import whois
    return whois.whois(domain)
