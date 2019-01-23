from grips.models import grips as grips_dao
from grips.models import user_grips as user_grips_dao
from users.services import users as user_service

def get_by_id(grip_id):
    return grips_dao.get_by_id(grip_id)

def get_by_search(user_email, search_term):
    return grips_dao.search(get_all_visible_by_user(user_email), search_term)

def get_all_visible_by_user(user_email):
    individual_grips = grips_dao.get_by_owner(user_email)
    org = user_service.get_current_org(user_email)
    if org is None:
        return individual_grips
    return individual_grips | grips_dao.get_by_owner(org.id)

def is_readable(grip, user_email):
    return grip.created_by == user_email or \
        user_service.is_in_org(user_email, grip.owned_by)

def is_editable_by(grip, user_email):
    return grip.created_by == user_email or \
        user_service.is_admin(user_email, grip.owned_by)

def is_shared(grip):
    return grip.created_by != grip.owned_by

def set_sharing(grip, user_email, to_share):
    if is_shared(grip) == to_share:
        return grip
    if to_share:
        current_user_org = user_service.get_current_org(user_email)
        return share(grip, current_user_org.id)

    return unshare(grip)

def has_voted_by(grip, user_email):
    user_grip = user_grips_dao.get_by_user_and_grip(user_email, grip.id)
    if user_grip is None:
        return False
    return user_grip.has_voted

def is_pinned_by(grip, user_email):
    user_grip = user_grips_dao.get_by_user_and_grip(user_email, grip.id)
    if user_grip is None:
        return False
    return user_grip.is_pinned

def get_votes(grip):
    return user_grips_dao.get_votes_by_grip(grip.id)

def set_voting(grip, user_email, to_vote):
    user_grip = user_grips_dao.upsert(user_email, grip, has_voted=to_vote)

def set_pin(grip, user_email, to_pin):
    user_grip = user_grips_dao.upsert(user_email, grip, is_pinned=to_pin)

def unshare(grip):
    grip.owned_by = grip.created_by
    return grips_dao.save(grip)

def share(grip, org_id):
    grip.owned_by = org_id
    return grips_dao.save(grip)

def delete(grip):
    grip.deleted = True
    grips_dao.save(grip)

def create(title, content, source, creator, to_share):
    owner = user_service.get_current_org(creator).id if to_share else creator
    return grips_dao.save(grips_dao.create_one(
        title=title,
        content=content,
        created_by=creator,
        source=source,
        owned_by=owner))
