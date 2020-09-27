from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'bloghome.html')
def blogPost(request,slug):
    return render(request,'blogpost.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.error(request,'please fill form correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'your message has been sent successfully')

    return render(request,'contact.html') 