from django.core.exceptions import ObjectDoesNotExist
from users.models import user_organizations as user_orgs_dao
from users.models import users as users_dao

def join_org_with_role(user_email, org, role):
    return user_orgs_dao.save(user_orgs_dao.create_one(
        user=users_dao.get_by_email(user_email),
        organization=org,
        role=role.name
    ))

def make_admin(user_email, org):
    return join_org_with_role(user_email, org, user_orgs_dao.Role.ADMIN)
