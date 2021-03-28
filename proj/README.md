# celery


celery start :- celery -A proj worker -l INFO
celery monitor flower :- celery -A proj flower   
                     http://127.0.0.1:5555/tasks
rabbitmq  monitor :-   http://127.0.0.1:15672/#/connections