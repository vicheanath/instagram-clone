import graphene
import graphql_jwt
from apps.users.models import User
from apps.graphql.users.mutations.mutations import UserType
from .mutations.mutations import (Register, VerifyAccount, ResendActivationEmail, SendPasswordResetEmail, PasswordReset, PasswordChange, UpdateAccount)

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType, description="List of all users")
    user = graphene.Field(UserType, id=graphene.Int(), description="Get user by ID")
    node = graphene.relay.Node.Field(description="A node with an ID")
    me = graphene.Field(UserType , description="Get the current user")

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in!")
        return user


class UserMutation(graphene.ObjectType):
    register = Register.Field()
    verify_account = VerifyAccount.Field()
    resend_activation_email = ResendActivationEmail.Field()
    send_password_reset_email = SendPasswordResetEmail.Field()
    password_reset = PasswordReset.Field()
    password_change = PasswordChange.Field()
    update_account = UpdateAccount.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
