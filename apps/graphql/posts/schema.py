import graphene

from apps.posts.models import Post
from .mutations import CreatePost, UpdatePost, DeletePost, SavePost, UnsavePost
from .types import PostType


class PostQuery(graphene.ObjectType):
    posts = graphene.List(PostType, description="List of all posts")

    def resolve_posts(self, info):
        return Post.objects.all()



class PostMutation(graphene.ObjectType):
    create_post = CreatePost.Field(description="Create a new post")
    update_post = UpdatePost.Field( description="Update a post")
    delete_post = DeletePost.Field(description="Delete a post")
    save_post = SavePost.Field(description="Save a post")
    unsave_post = UnsavePost.Field()
    
    
    
    