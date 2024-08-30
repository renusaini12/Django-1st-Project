from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Cont

# Create your views here.
def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def gallery(request):
    return render(request,'gallery.html',{})

def index(request):
    return render(request,'index.html',{})

def reservation(request):
    return render(request,'reservation.html',{})

def room(request):
    return render(request,'room.html',{})

def table(request):
    data = Cont.objects.all()
    data1 = {'data' : data}
    return render(request,'table.html',data1)  

def loginData(request):
    return render(request,'loginData.html',{})

def signUp(request):
    return render(request,'signUp.html',{})          

def signUpData(request):
    Name = request.POST.get('Name','default')
    Email = request.POST.get('Email','default')
    Subject = request.POST.get('subject','default')
    Contact = request.POST.get('Mobileno','default')
    print(Name,Email,Subject,Contact)


    u = Cont(Name=Name,Email=Email,Subject=Subject,Contact=Contact)
    u.save()

    # subject = 'welcome to GFG world'
    # message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['sainirenu703@gmail.com']
    # send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("Thanks for submit...")

def reservationData(request):
    Name = request.POST.get('Name','default')
    Email = request.POST.get('Email','default')
    Contact = request.POST.get('Mobileno','default')
    Date = request.POST.get('Date','default')
    Date1 = request.POST.get('Date1','default')
    Number = request.POST.get('Number','default')
    Number1 = request.POST.get('Number1','default')
    Room = request.POST.get('Room','default')
    Number2 = request.POST.get('Number2','default')
    print(Name,Email,Contact,Date,Date1,Number,Number1,Number2,Room)  
    return HttpResponse("Thanks for submit...") 

# def loginData(request):
#     Name = request.POST.get('Name','default')
#     Email = request.POST.get('Email','default')
#     Subject = request.POST.get('subject','default')
#     Contact = request.POST.get('Mobileno','default')
#     print(Name,Email,Subject,Contact) 
#     return HttpResponse("Thanks for submit...")

# def signUp(request):
#     Name = request.POST.get('name','default')
#     LastName = request.POST.get('lastname','default')
#     Email = request.POST.get('email','default')
#     print(Name,LastName,Email)
#     return HttpResponse("thanks for submit...")       


