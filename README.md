# zamanliMail

 ### Hem django hem worker hemde beat çalışıcak

kodları:
py manage.py runserver,
celery -A mailler beat -l info,
celery -A mailler worker -l info --pool=solo
