from django.contrib import admin
from django.urls import path, include
from .views import HomeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('accounts/google/login/', include('allauth.urls'), name="google_login"),    
    path('',HomeView, name="home")
]
