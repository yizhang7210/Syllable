from grips.models import grips as grips_dao

def get_all_by_user(user_email):
    return grips_dao.get_by_creator(user_email)

def get_by_id(grip_id):
    return grips_dao.get_by_id(grip_id)

def get_by_search(user_email, search_term):
    return grips_dao.get_by_search(user_email, search_term)
