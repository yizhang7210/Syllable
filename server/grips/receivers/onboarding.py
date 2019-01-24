from django.dispatch import receiver
from users.signals import users as user_signals
from grips.services import grips as grips_service

@receiver(user_signals.USER_SIGNED_UP)
def on_user_signed_up(sender, **kwargs):
    grips_service.create_user_guide(kwargs['user'].email)

@receiver(user_signals.USER_JOINED_ORG)
def on_user_joined_org(sender, **kwargs):
    grips_service.create_org_guide(kwargs['user'].email, kwargs['org'])
