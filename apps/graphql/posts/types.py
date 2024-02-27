
from apps.posts.models import Post
from graphene_django import DjangoObjectType

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'
        
    