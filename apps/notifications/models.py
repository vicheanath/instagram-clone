from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    target_id = models.PositiveIntegerField()
    target_type = models.CharField(max_length=10)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.type} - {self.target_type} - {self.target_id}'
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'type', 'target_id', 'target_type']