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

def is_readable(grip, user_email):
    return grip.created_by == user_email or \
        user_service.is_in_org(user_email, grip.owned_by)

def is_editable_by(grip, user_email):
    return grip.created_by == user_email or \
        user_service.is_admin(user_email, grip.owned_by)

def is_shared(grip):
    return grip.created_by != grip.owned_by

def get_votes(grip):
    return user_grips_dao.get_votes_by_grip(grip.id)

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

def set_sharing(grip, user_email, to_share):
    if is_shared(grip) == to_share:
        return grip
    if to_share:
        current_user_org = user_service.get_current_org(user_email)
        return share_with(grip, current_user_org.id)

    return unshare(grip)

def set_voting(grip, user_email, to_vote):
    user_grip = user_grips_dao.upsert(user_email, grip, has_voted=to_vote)

def set_pin(grip, user_email, to_pin):
    user_grip = user_grips_dao.upsert(user_email, grip, is_pinned=to_pin)

def share_with(grip, org_id):
    grip.owned_by = org_id
    return grips_dao.save(grip)

def unshare(grip):
    grip.owned_by = grip.created_by
    return grips_dao.save(grip)

def create_user_guide(user_email):
    title = "Welcome to Syllable!"
    content = (
    "1. This is a piece of knowledge, i.e. a Grip\n"
    "2. <------ Over THERE is how you create a Grip\n"
    "3. Pin/Delete on the left\n"
    "4. Source of the grip comes from below\n"
    "5. You only have 300 characters\n"
    "6. Invite your team on the top left\n\n\n"
    "And Enjoy!"
    )
    source = "support@acre.one"
    grip = create(title, content, source, user_email, False)
    set_pin(grip, user_email, True)

def create_org_guide(user_email, org):
    title = "You made it to the Team!"
    content = (
    "1. Now you can share Grips! (on the left)\n"
    "2. And vote!\n"
    "3. Green Grips are shared\n"
    "4. Red ones are private\n"
    "5. How about invite some more people?\n\n\n"
    "Now. Get a Grip. :)"
    )
    grip = grips_dao.save(grips_dao.create_one(
        title=title,
        content=content,
        created_by=user_email,
        source="support@acre.one",
        owned_by=org.id))
    set_pin(grip, user_email, True)
