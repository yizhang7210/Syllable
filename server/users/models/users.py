from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class User(models.Model):
    email = models.EmailField(max_length=50, unique=True, primary_key=True)
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.given_name + ':' + str(self.email)

def get_by_email(email):
    try:
        return User.objects.get(email=email)
    except ObjectDoesNotExist:
        return None

def create_one(**kwargs):
    return User(**kwargs)

def delete_all():
    return User.objects.all().delete()

def insert_many(users):
    User.objects.bulk_create(users)

def upsert(email, **kwargs):
    user = get_by_email(email)
    if user is None:
        user = User(email=email)

    for field in kwargs:
        setattr(user, field, kwargs[field])

    user.save()
    return user

def get_or_create(user):
    try:
        existing = User.objects.get(email=user.email)
        return existing
    except ObjectDoesNotExist:
        user.save()
        return user
