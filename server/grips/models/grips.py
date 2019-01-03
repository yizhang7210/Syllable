from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Grip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    created_by = models.EmailField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.created_by)

def get_by_creator(creator_email):
    return Grip.objects.filter(created_by=creator_email, deleted=False)

def get_by_id(id):
    try:
        return Grip.objects.get(id=id)
    except ObjectDoesNotExist:
        return None

def create_one(**kwargs):
    return Grip(**kwargs)

def save(grip):
    grip.save()
