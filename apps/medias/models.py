from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class Media(BaseModel):
    media = models.FileField(upload_to='media/%Y/%m/%d')
    description = models.TextField(blank=True)
    target_id = models.PositiveIntegerField()
    target_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} - {self.media}'

    class Meta:
        ordering = ['-created_at']
        
        

