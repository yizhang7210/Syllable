from django.dispatch import Signal

USER_SIGNED_UP = Signal(providing_args=['user'])

USER_JOINED_ORG = Signal(providing_args=['user', 'org'])
