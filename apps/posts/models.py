from django.db import models

from apps.users.models import User
from apps.core.models import BaseModel
from apps.medias.models import Media


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)
    reactions_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.caption}'


class Story(Post):
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        
class SavePost(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.post.caption}'
    
    class Meta:
        unique_together = ['user', 'post']