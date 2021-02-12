from django.db import models
import uuid
import os
# Create your models here.


def userimage_profile_file_path(instance, file_name):
    """Generate File path for new user image"""
    ext = file_name.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads", filename)


class File(models.Model):
    """Model for Images"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    file = models.ImageField(upload_to=userimage_profile_file_path)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} IMAGE"
