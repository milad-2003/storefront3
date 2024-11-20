from celery import shared_task
from time import sleep


@shared_task
def notify_customers(message):
    # Simulating a long task like sending 10 thousand emails
    print('Sending 10 thousand emails...')
    print(message)
    # Assuming that the task will take 10 seconds
    sleep(10)
    print('Emails were succussfully sent!')
