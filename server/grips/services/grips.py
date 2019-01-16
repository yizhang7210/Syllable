from grips.models import grips as grips_dao
from users.services import users as user_service

def get_all_visible_by_user(user_email):
    individual_grips = grips_dao.get_by_owner(user_email)
    org = user_service.get_current_org(user_email)
    if org is None:
        return individual_grips
    return individual_grips | grips_dao.get_by_owner(org.id)

def get_by_id(grip_id):
    return grips_dao.get_by_id(grip_id)

def get_by_search(user_email, search_term):
    return grips_dao.search(get_all_visible_by_user(user_email), search_term)

def is_editable(user_email, grip):
    return grip.created_by == user_email or \
        user_service.is_admin(user_email, grip.owned_by)

def is_shared(grip):
    return grip.created_by != grip.owned_by

def unshare(grip):
    grip.owned_by = grip.created_by
    return grips_dao.save(grip)

def share(grip, org_id):
    grip.owned_by = org_id
    return grips_dao.save(grip)

def delete(grip):
    grip.deleted = True
    grips_dao.save(grip)

def create(title, content, creator, is_shared):
    owner = user_service.get_current_org(creator).id if is_shared else creator
    return grips_dao.save(grips_dao.create_one(
        title=title,
        content=content,
        created_by=creator,
        owned_by=owner))
