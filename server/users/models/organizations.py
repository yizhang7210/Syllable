from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()
    domain = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return str(self.id) + ':' + self.name

def get_by_name(name):
    try:
        return Organization.objects.get(name=name)
    except ObjectDoesNotExist:
        return None

def get_by_id(org_id):
    try:
        return Organization.objects.get(id=org_id)
    except ObjectDoesNotExist:
        return None

def get_by_domain(domain):
    try:
        return Organization.objects.get(domain=domain)
    except ObjectDoesNotExist:
        return None

def create_one(**kwargs):
    return Organization(**kwargs)

def upsert(org_name, **kwargs):
    org = get_by_name(org_name)
    if org is None:
        org = Organization(name=org_name)

    for field in kwargs:
        setattr(org, field, kwargs[field])

    org.save()
    return org
