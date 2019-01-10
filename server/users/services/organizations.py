from django.core.exceptions import ObjectDoesNotExist
from users.models import organizations as orgs_dao

def create(org_name, creator):
    try:
        existing = orgs_dao.get_by_name(org_name)
        return None
    except ObjectDoesNotExist:
        new_org = orgs_dao.save(orgs_dao.create_one(
            name=org_name,
            created_by=creator
        ))
        return new_org

def get_by_id(id):
    return grips_dao.get_by_id(id)

def get_by_search(user_email, searchTerm):
    return grips_dao.get_by_search(user_email, searchTerm)
