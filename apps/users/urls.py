from django.urls import path, include
from .views import RegisterView, VerifyEmail, LoginView, LogoutView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('verify-email/<uidb64>/<token>/', VerifyEmail.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]