from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        msg = request.POST['massage']
        
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(msg)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, massage=msg)
            contact.save()
            messages.success(request, "Your message has been send")
        
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')
