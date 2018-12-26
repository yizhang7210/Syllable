from django.db import models

class Grip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.EmailField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.created_by)

def get_by_creator(creator_email):
    return Grip.objects.filter(created_by=creator_email)

def create_one(**kwargs):
    return Grip(**kwargs)
