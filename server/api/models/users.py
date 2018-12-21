from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ':' + str(self.email)

def get_by_email(email):
    return User.objects.get(email=email)

def create_one(**kwargs):
    return User(**kwargs)

def delete_all():
    return User.objects.all().delete()

def insert_many(users):
    User.objects.bulk_create(users)
