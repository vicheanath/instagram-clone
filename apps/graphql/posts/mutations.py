import graphene
from apps.posts.models import Post
from .types import PostType
from apps.users.models import User

class CreatePost(graphene.Mutation):
    class Arguments:
        caption = graphene.String(required=True)
        media = graphene.String(required=True)
        
    post = graphene.Field(PostType)
    
    def mutate(self, info, caption, media):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception("You must be logged in to create a post!")
        post = Post(caption=caption, media=media, author=user)
        post.save()
        return CreatePost(post=post)
    
class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        caption = graphene.String(required=True)
        media = graphene.String(required=True)
        
    post = graphene.Field(PostType)
    
    def mutate(self, info, id, caption, media):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception("You must be logged in to update a post!")
        post = Post.objects.get(pk=id)
        if post.author != user:
            raise Exception("You are not the author of this post!")
        post.caption = caption
        post.media = media
        post.save()
        return UpdatePost(post=post)
    
class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    post = graphene.Field(PostType)
    
    def mutate(self, info, id):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception("You must be logged in to delete a post!")
        post = Post.objects.get(pk=id)
        if post.author != user:
            raise Exception("You are not the author of this post!")
        post.delete()
        return DeletePost(post=None)

class SavePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    post = graphene.Field(PostType)
    
    def mutate(self, info, id):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception("You must be logged in to save a post!")
        post = Post.objects.get(pk=id)
        user.saved_posts.add(post)
        return SavePost(post=post)   
    
class UnsavePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        
    post = graphene.Field(PostType)
    
    def mutate(self, info, id):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception("You must be logged in to unsave a post!")
        post = Post.objects.get(pk=id)
        user.saved_posts.remove(post)
        return UnsavePost(post=post)
