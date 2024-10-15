from celery import Celery

import time


app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    print('Sleeping')
    time.sleep(5)
    print('Hello World')
    return 'Hello World'