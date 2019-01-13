from grips.models import grips as grips_dao
from users.services import users as user_service

def get_all_visible_by_user(user_email):
    org = user_service.get_current_org(user_email)
    return grips_dao.get_by_owner(user_email) | grips_dao.get_by_owner(org.id)

def get_by_id(grip_id):
    return grips_dao.get_by_id(grip_id)

def get_by_search(user_email, search_term):
    return grips_dao.search(get_all_visible_by_user(user_email), search_term)
