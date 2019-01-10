from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()

    def __str__(self):
        return self.name

def get_by_name(name):
    return Organization.objects.get(name=name)

def create_one(**kwargs):
    return Organization(**kwargs)

def delete_all():
    return Organization.objects.all().delete()

def insert_many(orgs):
    Organization.objects.bulk_create(orgs)

def save(org):
    org.save()
    return org
