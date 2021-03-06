from enum import Enum
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from .users import User
from .organizations import Organization

class Role(Enum):
    ADMIN = 'ADMIN'
    MEMBER = 'MEMBER'


class UserOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email + ' at ' + self.organization.name + ' with ' + self.role

    class Meta:
        unique_together = (('user', 'organization'), )

def get_by_user(user_email):
    try:
        return UserOrganization.objects.get(user=user_email)
    except ObjectDoesNotExist:
        return None

def get_by_org(org_id):
    return UserOrganization.objects.filter(organization=org_id)

def get_by_user_and_org(user_email, org_id):
    try:
        return UserOrganization.objects.get(user=user_email, organization=org_id)
    except ObjectDoesNotExist:
        return None

def delete_by_user_and_org(user_email, org_id):
    UserOrganization.objects.filter(user=user_email, organization=org_id).delete()

def create_one(**kwargs):
    return UserOrganization(**kwargs)

def upsert(user, org, **kwargs):
    user_org = get_by_user_and_org(user.email, org.id)
    if user_org is None:
        user_org = UserOrganization(user=user, organization=org)

    for field in kwargs:
        setattr(user_org, field, kwargs[field])

    user_org.save()
    return user_org

def get_or_create(user_org):
    try:
        existing = UserOrganization.objects.get(
            user=user_org.user,
            organization=user_org.organization)
        return existing
    except ObjectDoesNotExist:
        user_org.save()
        return user_org
