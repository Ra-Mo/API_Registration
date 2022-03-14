from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
import string
import random

# Create your views here.


msg = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        send_mail(
            'Activation Code',
            f'Hello {username} \n Your activating code is  {msg}',
            settings.EMAIL_HOST_USER, #
            [email], #
            fail_silently=False,
        )
        return render(request, 'activation.html')

    return render(request, 'user.html')


def activate(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == msg:
            return HttpResponse('Your account is activated')
        return HttpResponse('Wrong code ')
    return HttpResponse('Rien')








