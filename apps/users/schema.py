import graphene

from graphene_django import DjangoObjectType
from apps.users.models import User
from apps.users.mutations import Mutation, UserType


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)


schema = graphene.Schema(query=Query, mutation=Mutation)
