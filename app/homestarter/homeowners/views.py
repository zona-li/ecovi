from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from homeowners.forms import SignUpForm
from homeowners.tokens import account_activation_token
from django.http import HttpResponse
from django.core.mail import send_mail



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False                                          # Change the user.is_active to False, so the user can’t log in before confirming the email address
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Homelyfit Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject, message, 'zona@homelyfit.com', ['haoyang.zona@gmail.com'], fail_silently=False)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


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