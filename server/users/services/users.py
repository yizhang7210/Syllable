from users.models import user_organizations as user_orgs_dao
from users.models import users as users_dao
from users.models import organizations as orgs_dao
from users.signals import users as user_signals

def get_by_email(email):
    return users_dao.get_by_email(email)

def get_all_in_org(user_email):
    current_org = get_current_org(user_email)
    if not current_org:
        return []
    return [user_org.user for user_org in user_orgs_dao.get_by_org(current_org.id)]

def is_in_org(user_email, org_id):
    user_org = user_orgs_dao.get_by_user_and_org(user_email, org_id)
    return user_org is not None

def is_admin(user_email, org_id):
    user_org = user_orgs_dao.get_by_user_and_org(user_email, org_id)
    return user_org is not None and user_org.role == user_orgs_dao.Role.ADMIN

def get_current_org(user_email):
    user_org = user_orgs_dao.get_by_user(user_email)
    if user_org is None:
        return None

    return user_org.organization


def make_admin(user_email, org):
    join_org_with_role(user_email, org, user_orgs_dao.Role.ADMIN)

def join_org_with_role(user_email, org, role):
    user = users_dao.get_by_email(user_email)
    user_orgs_dao.save(user_orgs_dao.create_one(
        user=user,
        organization=org,
        role=role.name
    ))
    user_signals.USER_JOINED_ORG.send_robust(sender=__name__, user=user, org=org)

def remove_user_from_org(user_email, org_id):
    user_orgs_dao.delete_by_user_and_org(user_email, org_id)

def update_org_info(user_email, user_domain):
    current_user_org = get_current_org(user_email)
    if current_user_org is not None and current_user_org.domain != user_domain:
        remove_user_from_org(user_email, current_user_org.id)

    if user_domain is None:
        return

    org_with_domain = orgs_dao.get_by_domain(user_domain)
    if org_with_domain is not None and not is_in_org(user_email, org_with_domain.id):
        join_org_with_role(user_email, org_with_domain, user_orgs_dao.Role.MEMBER)
