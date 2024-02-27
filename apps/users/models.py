from ..core.models import BaseModel
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin,BaseModel):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email

    
    @classmethod
    def verify_account(cls, token):
      """Verify user account"""
      pass
       
    
    @classmethod
    def resend_activation_email(cls, email):
        """Resend activation email"""
        user = cls.objects.get(email=email)
        user.send_activation_email()
        
    def send_activation_email(self):
        pass
        
        
    @classmethod
    def send_password_reset_email(cls, email):
        pass
    
    @property
    def token(self):
        pass
    
    @property
    def token_expired(self):
        pass
    
    @property
    def reset_token(self):
        pass
    
    
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    cover = models.ImageField(upload_to="covers/", null=True, blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.user.email
    
    
class Follow(BaseModel):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    
    class Meta:
        unique_together = ['follower', 'following']
        
    def __str__(self):
        return f'{self.follower.email} - {self.following.email}'