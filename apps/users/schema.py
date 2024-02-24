import graphene

from graphene_django import DjangoObjectType
from apps.users.models import User
from apps.users.mutations import Mutation, UserType


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    node = graphene.relay.Node.Field()
    me = graphene.Field(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in!")
        return user


schema = graphene.Schema(query=Query, mutation=Mutation)
