from django.db import models

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

def save(org):
    org.save()
    return org
