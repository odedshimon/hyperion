# To run this celery worker from shell type: celery -A celery_worker.celery_app worker --loglevel=info

from celery import Celery
from hyperion_backend import flask_app


def make_celery(flask):
    app = Celery(
        flask.import_name,
        backend=flask.config['CELERY_RESULT_BACKEND'],
        broker=flask.config['CELERY_BROKER_URL']
    )

    class ContextTask(app.Task):
        def __call__(self, *args, **kwargs):
            with flask.app_context():
                return self.run(*args, **kwargs)

    app.Task = ContextTask
    return app


celery_app = make_celery(flask_app)



