from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created_date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title