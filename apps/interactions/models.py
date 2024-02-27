from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel
from apps.medias.models import Media

class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    target_id = models.PositiveIntegerField()
    target_type = models.CharField(max_length=10)
    

    def __str__(self):
        return f'{self.user.username} - {self.type} - {self.target_type} - {self.target_id}'