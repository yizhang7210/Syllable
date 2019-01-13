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

def update(org_id, updated_data):
    org = orgs_dao.get_by_id(org_id)
    return orgs_dao.update(org, updated_data)
