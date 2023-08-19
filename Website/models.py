from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField()

#     def __str__(self) -> str:
#         return self.first_name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # additional fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self) -> str:
        return self.user.username

class Topic(models.Model): # inherit from the Model class 
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self) -> str:
        return self.top_name
    

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=264, unique=False)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name
    

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)
