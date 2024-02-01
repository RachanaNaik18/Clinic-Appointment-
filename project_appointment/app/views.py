from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
class Home(View):
    def get(self, request):
        return render (request, 'base.html')


class Appoint(View):

    def get(self, request):
        if request.user.is_authenticated:
            data = Patients.objects.all()
            st = Timeslots.objects.all().values_list('slots', flat=True)
            booked = Patients.objects.all().values_list('slot', flat=True)
            return render(request, 'appoint.html', {'data':data, 'st':st, 'booked':booked})
        else:
            return HttpResponseRedirect('/u_signup/')
    
    def post(self, request):
        if request.user.is_authenticated:
        
            st = Timeslots.objects.all().values_list('slots', flat=True)
            booked_date = Patients.objects.all().values_list('app_date', flat=True)
            
            # print(booked_d)
            # booked_date= []
            # for i in booked_d:
            #     booked_date.append(str(i))
            print(booked_date)
            booked=Patients.objects.all().values_list('slot', flat=True)
            name=request.POST.get('name')
            age=request.POST.get('age')
            contact=request.POST.get('con')
            reason=request.POST.get("reason")
            app_date=request.POST.get('app_date')
            slot=request.POST.get('slot')
            i =0
            while i <= len(booked):
                if len(booked) == 0:
                    Patients.objects.create(name=name, age=age, contact=contact, reason=reason,  slot=slot, user=request.user, app_date=app_date) 
                if app_date != booked_date[i] or slot != booked[i]:
                    i+=1
                    if i == len(booked):
                        Patients.objects.create(name=name, age=age, contact=contact, reason=reason,  slot=slot, user=request.user, app_date=app_date)
                        print(type(app_date), type(booked_date), type(slot), type(booked))
                        messages.success(request, f"Your appointment is on {app_date} at {slot}")
                        break
                elif app_date == booked_date[i] and slot == booked[i]:
                    messages.success(request, "This slot is already booked please select Different slot")
                    break
                    

            data = Patients.objects.all()
        else:
            return HttpResponseRedirect('/u_signup/')
        return render(request, 'appoint.html', {'data':data, 'st':st, 'booked':booked, 'slotd':slot})


def Doctor(request):
    if request.user.is_authenticated and request.user.is_staff:
        data = Patients.objects.filter(user_id=request.user)
        return render(request, 'doctor.html', {'data':data})
    else:
        messages.success('Login only if you are the staff member')
        return HttpResponseRedirect('/d_signup/')

def History(request, id):
    a = Patients.objects.get(pk=id)
    Patients_history.objects.create(name=a.name, age=a.age, contact=a.contact, date=a.date, reason=a.reason, slot=a.slot)
    Patients.objects.get(pk=id).delete()
    return HttpResponseRedirect('/doctor/')

def Doc_Sign(request):
        if request.method == "POST":
            uname= request.POST.get('uname')
            email= request.POST.get('email')
            password= request.POST.get('password')
            u = User.objects.create_user(uname, email, password)
            u.is_staff=True
            u.save()
    
        return render(request, 'doc_signup.html')

def d_login(request):
    if request.method=="POST":
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            login(request, user)
    
        return HttpResponseRedirect('/doctor/')
    

def user_Sign(request):
        if request.method == "POST":
            uname= request.POST.get('uname')
            email= request.POST.get('email')
            password= request.POST.get('password')
            u = User.objects.create_user(uname, email, password)
            u.save()
    
        return render(request, 'user_signup.html')

def user_login(request):
    if request.method=="POST":
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            login(request, user)

        return HttpResponseRedirect('/appoint/')
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request, request.user)
        return HttpResponseRedirect('/u_signup/')

def DateFilter(request):
    if request.method=="POST":
        date = request.POST.get('date')
        a = Patients.objects.filter(app_date=date).values_list('slot',flat=True)
        b = Timeslots.objects.all().values_list('slots',flat=True)
        datas = []
        for i in b:
            if i not in a:
                datas.append(i)
        data = Patients.objects.all()
    return render(request,'appoint.html',{'datas':datas,'data':data})