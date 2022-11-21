import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from enums.templates_enum import TemplateEnum
from config.celery import app

UserModel = get_user_model()


class EmailUtils:
    @staticmethod
    @app.task
    def _send_email(to: str, template_name: str, context: dict, subject='') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register_email(cls, address: str, name: str, token: str) -> None:
        url = f'{os.environ.get("FRONTEND_HOST")}/activate/{token}'
        subject = 'Register mail'
        cls._send_email.delay(address, TemplateEnum.REGISTER.value, {'name': name, 'link': url}, subject)

    @classmethod
    def email_spam(cls):
        for user in UserModel.objects.all():
            cls._send_email(user.email, TemplateEnum.SPAM.value, {}, 'SPAM')
