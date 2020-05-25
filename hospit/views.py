from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
# Create your views here.
def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error='yes'
    d={'error':error}
    return render(request,'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)


def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        s=request.POST['special']
       
        try:
            Doctor.objects.create(name=n,mobile=c,special=s)
            error="no"
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')

    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)


def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        g=request.POST['gender']
        a=request.POST['address']
       
        try:
            Patient.objects.create(name=n,mobile=c,gender=g,address=a)
            error="no"
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')

    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)


def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        d1=request.POST['date']
        t1=request.POST['time']
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()
       
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t1)
            error="no"
        except:
            error='yes'
    d={'doctor':doctor1, 'patient':patient1, 'error':error}
    return render(request,'add_appointment.html',d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')

    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
