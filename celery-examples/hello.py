from celery import Celery


app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    print('Hello World')
