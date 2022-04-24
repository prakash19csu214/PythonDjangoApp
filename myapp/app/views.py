from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     name = "prakash"
#     return render(request,'index.html', context={'name':name})


def login(request):
    return render(request,'login.html')


def index(request):
    username = request.POST['u_name']
    password = request.POST['u_password']

    if username == "prakash" and password == "pk":
        msg = 'Login Successful'
    else :
        msg = 'Login Fail'
    
    return render(request, 'index.html', context = {'msg':msg, 'name':username})