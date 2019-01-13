from rest_framework import serializers
from users.models.users import User
from users.models import user_organizations as user_orgs_dao
from users.serializers.organizations import OrganizationSerializer

class UserSerializer(serializers.ModelSerializer):

    organization = serializers.SerializerMethodField('get_org')

    # pylint: disable=no-self-use
    def get_org(self, user):
        user_orgs = user_orgs_dao.get_by_user(user.email)
        if not user_orgs:
            return None

        user_org = user_orgs[0]
        org = OrganizationSerializer(user_org.organization).data
        org['role'] = user_org.role
        return org

    class Meta:
        model = User
        fields = ('email', 'family_name', 'given_name', 'created_at', 'organization')
