from .final_spoj  import scraper
from django.shortcuts import render
from codedigger.settings import EMAIL_HOST_USER
from django.core.mail import send_mail	

def my_cron_job():
    #checking if cronjobs has started , you will get a mail
    subject = 'SPOJ Scraping Started'
    message = 'Hope you are enjoying our Problems'
    recepient = 'aaradhyaberi@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    scraper()
    subject = 'SPOJ Scraping Finished'
    message = 'Hope you are enjoying our Problems'
    recepient = 'aaradhyaberi@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)