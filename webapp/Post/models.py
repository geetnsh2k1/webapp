from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    created = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='created')
    
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200, null=False)
    data = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=False, blank=False)
    location = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="Event/", default='Event/default.jpg')
    
    is_liked = models.ManyToManyField(to=User, related_name='is_liked', null=True, blank=True)
    
    def __str__(self):
        return self.event_name + ' - ' + self.created.username
    