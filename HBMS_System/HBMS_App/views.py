from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import connection
from.models import admin1, employee1
import hashlib
from django.db.models import Q

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

#admin -> add emlpoyees into database
def addemployees(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin1.objects.get(phone = current_user)
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            dept = request.POST.get('dept')
            address = request.POST.get('address')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            if(password == cpassword):
                if employee1.objects.filter(email = email).count():
                    sms = 'This email already exits!'
                    param = {
                        'sms' : sms,
                        'current_user' : data,
                    }
                    return render(request, 'admin_home.html', param)
                elif employee1.objects.filter(phone = phone).count():
                    sms = 'This Phone Number already exits!'
                    param = {
                        'sms' : sms,
                        'current_user' : data,
                    }
                    return render(request, 'admin_home.html', param)
                else:
                    hash = hashlib.md5(password.encode())
                    pass1 = hash.hexdigest()
                    save_emp = employee1(name = name, email = email, phone = phone, gender = gender, department = dept, address = address, password = pass1)
                    save_emp.save()
                    sms1 = 'Employee Data Saved Successfully!'
                    param = {
                        'sms1' : sms1,
                        'current_user' : data,
                    }
                    return render(request, 'admin_home.html', param)
            else:
                sms = 'Password and Confirm password did not match, please try again!'
                param = {
                    'current_user' : data,
                    'sms' : sms,
                }
                return render(request, 'admin_home.html', param)
        return render(request, 'admin_home.html')
    return redirect('admin')

#admin -> show employee list showemp.html
def show_emp(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin1.objects.get(phone = current_user)
        emp = employee1.objects.all()
        param = {
            'current_user' : data,
            'emp' : emp,
        }
        return render(request, 'showemp.html', param)
    return redirect('admin')

#admin -> emlpoyees delete,
def emp_delete(request, id):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin1.objects.get(phone = current_user)
        del_emp = employee1.objects.get(id = id)
        del_emp.delete()
        emp = employee1.objects.all()
        sms = 'Deleted records successfully!'
        param = {
            'current_user' : data,
            'emp' : emp,
            'sms' : sms,
        }
        return render(request, 'showemp.html', param)
    return redirect('admin')

#admin -> emplpyees edit form
def emp_edit(request, id):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin1.objects.get(phone = current_user)
        edit = employee1.objects.get(id = id)
        param = {
            'current_user' : data,
            'edit' : edit,
        }
        return render(request, 'empedit.html', param)
    return redirect('admin')

#admin -> employee records update from empedit.html
def update_emp(request):
    if 'check_logged' in request.session:
        current_user = request.session['check_logged']
        data = admin1.objects.get(phone = current_user)
        if request.method == 'POST':
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            department = request.POST.get('department')
            address = request.POST.get('address')
            update_data = employee1.objects.filter(id = id).update(name = name, email = email, phone = phone, gender = gender, department = department, address = address)
            emp = employee1.objects.all()
            if(update_data):
                sms = 'Update records successfully!'
                param = {
                    'current_user' : data,
                    'sms' : sms,
                    'emp' : emp,
                }
                return render(request, 'showemp.html', param)
            else:
                return redirect('show_emp')
        else:
            sms = 'Some problems were encountered!'
            param = {
                'current_user' : data,
                'sms1' : sms,
            }
        return render(request, 'showemp.html', param)
    return redirect('admin')      


