from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from .grips import Grip

class UserGrip(models.Model):
    user = models.EmailField(db_index=True) # No cross app reference
    grip = models.ForeignKey(Grip, on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user + ':' + str(self.grip.title)

    class Meta:
        unique_together = (('user', 'grip'), )

def get_by_user_and_grip(user_email, grip_id):
    try:
        return UserGrip.objects.get(user=user_email, grip=grip_id)
    except ObjectDoesNotExist:
        return None

def get_by_id(user_grip_id):
    try:
        return UserGrip.objects.get(id=user_grip_id)
    except ObjectDoesNotExist:
        return None

def get_votes_by_grip(grip_id):
    return len(UserGrip.objects.filter(grip=grip_id, has_voted=True))

def create_one(**kwargs):
    return UserGrip(**kwargs)

def upsert(user_email, grip, **kwargs):
    user_grip = get_by_user_and_grip(user_email, grip.id)
    if user_grip is None:
        user_grip = UserGrip(user=user_email, grip=grip)

    for field in kwargs:
        setattr(user_grip, field, kwargs[field])

    user_grip.save()
