from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection
from.models import admin1

# Create your views here.
#first page after server on
def index(request):
    return render(request, 'index.html')

#goto -> admin.html page
def admin(request):
    return render(request, 'admin.html');

#admin_home -> controls sessions
def admin_home(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin1.objects.get(phone = current_user)
        param = {
            'current_user' : data,
        }
        return render(request, 'admin_home.html', param)
    else:
        return redirect('index')
    return redirect('index')

#admin login functions
def adminlogin(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        pwd = request.POST.get('password')
        check_user = admin1.objects.filter(phone = phone, password = pwd)
        if check_user:
            request.session['check_logged'] = phone
            return redirect('admin_home')
        else:
            sms = 'Invalid user id or password!'
            return render(request, 'admin.html', { 'sms' : sms })
        return render('index')

#admin logout
def adminlogout(request):
    try:
        del request.session['check_logged']
    except:
        return redirect('index')
    return redirect('index')
