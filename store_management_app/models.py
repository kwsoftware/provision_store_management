from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    user_type_data = ((1, "Superuser"),(2, "Normaluser"))
    user_type = models.CharField(choices=user_type_data, default=1, max_length=12)

class Superuser(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user_design.username}'

class Normaluser(models.Model):
    main_id = models.AutoField(primary_key=True)
    user_design = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user_design.username}'

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Superuser.objects.create(user_design=instance, mobile_no="")
        if instance.user_type==2:
            Normaluser.objects.create(user_design=instance, mobile_no="")
        

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.superuser.save()
    if instance.user_type==2:
        instance.normaluser.save()
