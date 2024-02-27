import graphene
from .users.schema import UserQuery, UserMutation
from .posts.schema import PostQuery, PostMutation


class Query(UserQuery, PostQuery):
    pass


class Mutation(UserMutation, PostMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
