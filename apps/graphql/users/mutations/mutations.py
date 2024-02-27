import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from apps.users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password",)

class Register(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        name = graphene.String(required=True)
        username = graphene.String(required=True)
        
    user = graphene.Field(UserType)
    
    def mutate(self, info, email, password, name, username):
        user = User.objects.create_user(email=email, password=password, name=name, username=username)
        return Register(user=user)
    
class VerifyAccount(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        
    user = graphene.Field(UserType)
    
    def mutate(self, info, token):
        user = User.objects.verify_account(token)
        return VerifyAccount(user=user)
    
class ResendActivationEmail(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, email):
        User.objects.resend_activation_email(email)
        return ResendActivationEmail(success=True)
    
class SendPasswordResetEmail(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, email):
        User.objects.send_password_reset_email(email)
        return SendPasswordResetEmail(success=True)
    
class PasswordReset(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        new_password = graphene.String(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, token, new_password):
        User.objects.password_reset(token, new_password)
        return PasswordReset(success=True)
    
class PasswordChange(graphene.Mutation):
    class Arguments:
        old_password = graphene.String(required=True)
        new_password = graphene.String(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, old_password, new_password):
        user = info.context.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return PasswordChange(success=True)
        else:
            return PasswordChange(success=False)
        
class UpdateAccount(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        email = graphene.String()
        name = graphene.String()
        username = graphene.String()
        bio = graphene.String()
        website = graphene.String()
        location = graphene.String()
        birth_date = graphene.Date()
        
    user = graphene.Field(UserType)
    
    def mutate(self, info, **kwargs):
        user = User.objects.get(id=kwargs.get("id"))
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return UpdateAccount(user=user)
    
class ObtainJSONWebToken(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        
    token = graphene.String()
    
    def mutate(self, info, email, password):
        user = User.objects.get(email=email)
        if user.check_password(password):
            return ObtainJSONWebToken(token=user.token)
        else:
            return ObtainJSONWebToken(token=None)
        
class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        username = graphene.String()
        
    token = graphene.String()
    refresh_token = graphene.String()
    
    def mutate(self, info, email, password):
        user = User.objects.get(email=email)
        if user.check_password(password):
            return Login(token=user.token, refresh_token=user.refresh_token)
        else:
            return Login(token=None, refresh_token=None)
        

    
