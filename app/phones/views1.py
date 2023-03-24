from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .forms import UserRegistrationForm
from .passwords import generate_password
from .serializer import RegisterS2,SetPassword_No
from .tokens import account_activation_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.first_name = ''
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('http://smartshopcenter.org:3000/sign-in')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('http://smartshopcenter.org:3000/sign-in')

def reset(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.set_password(user.first_name)
        user.first_name = ''
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('http://smartshopcenter.org:3000/sign-in')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('http://smartshopcenter.org:3000/sign-in')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'password':user.first_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')
def RedirectEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_reset_password.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')
@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
        )
class ApiCreate2(APIView):
    permission_classes = ()
    def post(self,request):
        serializer = RegisterS2(data=request.data)
        if serializer.is_valid(raise_exception=True):
            password = generate_password()
            user = serializer.save()
            user.set_password(password)
            user.first_name = password
            user.is_active = False
            user.save()
            activateEmail(request, user, user.email)
            return Response('ok')
class ApiForgetPssword(APIView):
    permission_classes = ()
    def post(self,request):
        serializer = SetPassword_No(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        RedirectEmail(request, user, user.email)
        return Response('ok')

def login(request):
    return render(request, 'login.html')
def auth(request):
    return render(request, 'login1.html')
@login_required
def home(request):
    return render(request, 'home.html')