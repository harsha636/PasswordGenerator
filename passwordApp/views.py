
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
    char = list('')
    length = int(request.GET.get('length'))

    if(length<6):
        return render(request, 'home.html', {'error':'Password length must be greater than or equal to 6.'})

    if(length>=6):
            if request.GET.get('uppercase'):
                char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

            if request.GET.get('lowercase'):
                char.extend(list('abcdefghijklmnopqrstuvwxyz'))

            if request.GET.get('digits'):
                char.extend(list('0123456789'))

            if request.GET.get('symbols'):
                char.extend(list('!#$%^&*()[]\/<>?|@'))
            
            random_password = ''
            for i in range(length):
                random_password += random.choice(char)
            return render(request, 'password.html', {'password':random_password})
    
    