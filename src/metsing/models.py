from uuid import uuid4

from django.db import models
from model_utils.models import TimeStampedModel


class User(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=16)

    def __str__(self):
        return self.full_name
