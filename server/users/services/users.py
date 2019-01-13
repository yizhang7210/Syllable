from users.models import user_organizations as user_orgs_dao
from users.models import users as users_dao
from users.models import organizations as orgs_dao

def join_org_with_role(user_email, org, role):
    return user_orgs_dao.save(user_orgs_dao.create_one(
        user=users_dao.get_by_email(user_email),
        organization=org,
        role=role.name
    ))

def make_admin(user_email, org):
    return join_org_with_role(user_email, org, user_orgs_dao.Role.ADMIN)

def has_org(user_email):
    return user_orgs_dao.get_by_user(user_email) is not None

def remove_user_from_org(user_email, org_id):
    user_orgs_dao.delete_by_user_and_org(user_email, org_id)

def get_current_org(user_email):
    user_org = user_orgs_dao.get_by_user(user_email)
    if user_org is None:
        return None

    return user_org.organization

def is_in_org(user_email, org_id):
    user_org = user_orgs_dao.get_by_user_and_org(user_email, org_id)
    return user_org is not None

def get_by_email(email):
    return users_dao.get_by_email(email)

def update_org_info(user_email, user_domain):
    current_user_org = get_current_org(user_email)
    if current_user_org is not None and current_user_org.domain != user_domain:
        remove_user_from_org(user_email, current_user_org.id)

    if user_domain is None:
        return

    org_with_domain = orgs_dao.get_by_domain(user_domain)
    if org_with_domain is not None and not is_in_org(user_email, org_with_domain.id):
        join_org_with_role(user_email, org_with_domain, user_orgs_dao.Role.MEMBER)
