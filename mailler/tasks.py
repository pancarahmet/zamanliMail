from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings

@shared_task
def send_test_mail():
    print("Fonksiyon çalıştı")
    subject="Merhabaaa"
    msg="bu bir deneme mailidir aloooooooooooooooooooo"
    from_email=settings.EMAIL_HOST_USER
    recipent_list=["pancarahmet@gmail.com","hakan.mollaahmetoglu@gmail.com"]
    send_mail(subject,msg,from_email,recipent_list,fail_silently=False)
    return "Mail Göndreldi"