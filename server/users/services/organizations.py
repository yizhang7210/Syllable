from users.models import organizations as orgs_dao
from users.models import users as users_dao
from users.models import user_organizations as user_orgs_dao

def create(org_name, creator):
    existing = orgs_dao.get_by_name(org_name)
    if existing is not None:
        return None

    new_org = orgs_dao.save(orgs_dao.create_one(
        name=org_name,
        created_by=creator
    ))
    return new_org

def update(org_id, updated_data):
    org = orgs_dao.get_by_id(org_id)
    return orgs_dao.update(org, updated_data)

def invite(org_id, emails):
    if not emails:
        return;
    org = orgs_dao.get_by_id(org_id)
    for email in emails:
        user = users_dao.get_or_create(users_dao.create_one(email=email))
        user_orgs_dao.upsert(user_orgs_dao.create_one(
            user=user,
            organization=org,
            role=user_orgs_dao.Role.MEMBER.name
        ))
