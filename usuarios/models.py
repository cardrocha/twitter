from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField("self",
    related_name="followed_by", 
    symmetrical=False, 
    blank=True)
  bio = models.CharField(max_length=50)
  profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
  
  date_modified = models.DateTimeField(User, auto_now=True)
  
  def __str__(self):
    return self.user.username
# @receiver(post_save, sender=User)  
def create_profile(sender, instance, created, **kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()

    user_profile.follows.set([instance.profile.id])
    user_profile.save()

post_save.connect(create_profile, sender=User)