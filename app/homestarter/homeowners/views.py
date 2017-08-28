from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from homeowners.forms import SignUpForm
from homeowners.tokens import account_activation_token
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from decouple import config

# To use Sendgrid
import sendgrid
import os
from sendgrid.helpers.mail import *


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False                                          # Change the user.is_active to False, so the user can’t log in before confirming the email address
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your EcoVi Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # sendEmail();
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def sendEmail():
    ################### Using Sendgrid ###################
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(config('SENDGRID_API_KEY')))
    from_email = Email("haoyang.zona@gmail.com")
    to_email = Email("haoyang.zona@gmail.com")
    subject = "Testing SendGrid"
    content = Content("text/plain", "This is the content")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

def account_activation_sent(request):
    html = "<html><body>Please confirm your email address to complete the signup.</body></html>"
    return HttpResponse(html)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.homeowner.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('main/index')
    else:
        return render(request, 'account_activation_invalid.html')