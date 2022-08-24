from django.shortcuts import render
from django.http import HttpResponse
from .models import contact,Blogpost
import pprint
def index(request):
    mypost = Blogpost.objects.all()
    return render(request,'shop/index.html',{'mypost':mypost})

def about(request):
    return render(request,'shop/about.html')

def post(request,id):
    pos = Blogpost.objects.filter(post_id=id)[0]
    return render(request, 'shop/post.html', {'post': pos})

def CONTACT(request):
    thank =False
    if request.method == "POST":
        name=request.POST.get('nam','')
        lname=request.POST.get('lnam','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        problem=request.POST.get('problem','')
        help_desc=request.POST.get('help','')
        #help= pprint.pprint(help_desc)
        contacts = contact(name=name, lname=lname, email=email, phone=phone, problem=problem, desc=help_desc)
        contacts.save()
        thank = True
        
    return render(request, 'shop/contact.html',{'thank':thank})