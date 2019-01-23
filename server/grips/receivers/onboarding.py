from django.dispatch import receiver
from users.signals import users as user_signals

@receiver(user_signals.USER_SIGNED_UP)
def on_user_signed_up(sender, **kwargs):
    print("user created")
    print(sender)
    print(kwargs)


@receiver(user_signals.USER_JOINED_ORG)
def on_user_joined_org(sender, **kwargs):
    print("user joined org")
