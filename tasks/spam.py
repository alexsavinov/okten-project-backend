from config.celery import app
from utils.email_util import EmailUtils


@app.task
def spam_email():
    EmailUtils.email_spam()
