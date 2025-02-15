from .models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views import View
# from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse,JsonResponse

class RegisterView(View):
    def get(self, request):
        return render(request, 'users/signup/signup.html')

    def post(self, request):
        username = request.POST['username']
        fullname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email already in use"}, status=400)

        user = User.objects.create_user(username=username, full_name=fullname, email=email, password=password, is_active=False)

        # Email Verification
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain
        # link = f"http://{domain}/users/verify-email/{uid}/{token}/"

        subject = "Verify Your Email"
        html_message = render_to_string("users/verifications/email_verification.html", {
            "user": user,
            "link":f"http://{domain}/users/verify-email/{uid}/{token}/"
        })
        plain_message = strip_tags(html_message)
        email = EmailMultiAlternatives(subject, plain_message, "techtitatns@gmail.com", [email])

        email.attach_alternative(html_message, "text/html")  # Attach the HTML version
        email.send()
        return JsonResponse({"success": True, "message": "Please check your email to verify your account."}, status=400)

class VerifyEmail(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse("Email verified. You can now log in.")
        return HttpResponse("Invalid or expired link.")
    
class LoginView(View):
    def get(self, request):
        return render(request, 'users/login/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user and user.is_active:
            login(request, user)
            return redirect('home')
        return HttpResponse("Invalid credentials or email not verified.")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
