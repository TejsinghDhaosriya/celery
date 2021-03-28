from celery import Celery

app = Celery('tasks',backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.task_serializer = 'json'
@app.task
def add(x, y):
    return x + y