from django.urls import path
from store_management_app import views, admin_views, user_views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("register/", views.render_register, name="render_register"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("perform_register", views.perform_register, name="perform_register"),
    path("perform_logout", views.perform_logout, name="perform_logout"),
    path("dashboard/", admin_views.render_dashboard, name="render_dashboard"),
    path("user_dashboard/", user_views.render_dashboard, name="render_user_dashboard"),
]