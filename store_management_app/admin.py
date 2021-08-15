from django.contrib import admin
from store_management_app import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Superuser)
admin.site.register(models.Normaluser)