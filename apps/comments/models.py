from django.db import models

from apps.users.models import User
from apps.core.models import BaseModel
from apps.medias.models import Media

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    content = models.TextField()
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    reactions_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.content}'
