from django.urls import path
from store_management_app import views

urlpatterns = [
    path("", views.render_login, name="render_login"),
]