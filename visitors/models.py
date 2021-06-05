from django.db import models
from user.models import User
# Create your models here.

class Visitor(models.Model):
    name = models.CharField(max_length=255)
    document_id = models.CharField(max_length=255)
    document_picture = models.ImageField()
    picture = models.ImageField()

    invited_by = models.ForeignKey(User)