from django.db import models

from helpers.models import TrackingModel
from authentication.models import User


class Todo(TrackingModel):

    title = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
