from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()
    domain = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

def get_by_name(name):
    return Organization.objects.get(name=name)

def get_by_id(id):
    return Organization.objects.get(id=id)

def create_one(**kwargs):
    return Organization(**kwargs)

def update(org, updated_data):
    for field in updated_data:
        if isUpdatable(field):
            setattr(org, field, updated_data[field])
    return save(org)

def save(org):
    org.save()
    return org

def isUpdatable(field):
    return field in ['name', 'domain']
