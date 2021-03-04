from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    image_url= models.ImageField(upload_to='photoshare/media')
    bio = models.CharField(max_length=1000)


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoshare/media')
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
