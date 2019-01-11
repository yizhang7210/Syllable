from enum import Enum
from django.db import models
from .users import User
from .organizations import Organization

class Role(Enum):
    ADMIN = 'ADMIN'


class UserOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user + ' at ' + self.organization + ' with ' + self.role

    class Meta:
        unique_together = (('user', 'organization'), )

def get_by_user(user_email):
    return UserOrganization.objects.filter(user=user_email)

def create_one(**kwargs):
    return UserOrganization(**kwargs)

def save(user_org):
    user_org.save()
    return user_org
