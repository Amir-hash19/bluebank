from django.urls import path
from .views import show_user_page, show_info

urlpatterns = [
    path("info", show_info),
    path("user/<str:name>", show_user_page),
    
]