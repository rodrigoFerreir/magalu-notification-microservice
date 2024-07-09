from django.db import models
import uuid


class BaseClassModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        abstract = True
