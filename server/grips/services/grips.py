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
