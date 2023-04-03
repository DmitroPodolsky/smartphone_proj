from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from .passwords import generate_password
from .serializer import RegisterS2, SetPassword_No
from .tokens import account_activation_token


def activate_simple(uid):
    User = get_user_model()
    try:
        return User.objects.get(pk=uid)
    except:
        return None


def activate(request, uidb64, token):
    user = activate_simple(force_str(urlsafe_base64_decode(uidb64)))
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.first_name = ''
        user.save()
    return redirect('http://localhost:3000')#'http://smartshopcenter.org:3000/sign-in'


def reset(request, uidb64, token):
    user = activate_simple(force_str(urlsafe_base64_decode(uidb64)))
    if user is not None and account_activation_token.check_token(user, token):
        user.set_password(user.first_name)
        user.first_name = ''
        user.save()
    return redirect('http://localhost:3000')#'http://smartshopcenter.org:3000/sign-in'


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'password': user.first_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    #email = EmailMessage(mail_subject, message, to=[to_email])
    send_mail(
                        subject=mail_subject,
                        message=f"к сожалению данного продукта пока нету в наличии. вся оплата будет возращена за данный товар. С вами свяжеться техническая поддержка в ближайшое время доставки в ближайшое время",
                        recipient_list=[to_email],
                        from_email="matt@test.com",
                        fail_silently=True,
                        html_message=message
                    )
    '''if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')'''


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


class Api_Create_Account(APIView):
    permission_classes = ()

    def post(self, request):
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

    def post(self, request):
        serializer = SetPassword_No(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        RedirectEmail(request, user, user.email)
        return Response('ok')
