from users.models import organizations as orgs_dao
from users.models import users as users_dao
from users.models import user_organizations as user_orgs_dao
from users.utils import notifications

def create(org_name, creator):
    existing = orgs_dao.get_by_name(org_name)
    if existing is not None:
        return None

    new_org = orgs_dao.upsert(org_name, created_by=creator)
    return new_org

def change_domain(org, new_domain):
    return orgs_dao.upsert(org.name, domain=new_domain)

def invite(invitor, org_id, emails):
    if not emails:
        return
    org = orgs_dao.get_by_id(org_id)
    for email in emails:
        user = users_dao.get_or_create(users_dao.create_one(email=email))
        user_orgs_dao.get_or_create(user_orgs_dao.create_one(
            user=user,
            organization=org,
            role=user_orgs_dao.Role.MEMBER.name
        ))
    notifications.notify_invite(invitor, org, emails)
