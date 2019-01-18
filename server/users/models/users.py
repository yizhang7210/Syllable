from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class User(models.Model):
    email = models.EmailField(max_length=50, unique=True, primary_key=True)
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField()

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

def upsert(user):
    try:
        existing = User.objects.get(email=user.email)
        existing.family_name = user.family_name
        existing.given_name = user.given_name
        existing.last_active_at = user.last_active_at
        existing.save()
    except ObjectDoesNotExist:
        user.save()
