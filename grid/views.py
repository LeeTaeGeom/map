from users.views import myinfo
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from .acci_type.type import *
# Create your views here.

def show(request):

    trenches=Trench.objects.all()

    return render(request,'map.html',{"trenches":trenches})

def ifr(request):
    return render(request,'iframemap.html')

def hi(requset):
    a=Trench.objects.all()
    for i in a:
        print(i.trench_num)
        print(i.longitude)
        print(i.latitude)
    return HttpResponse('hi') 
    
def testjq(request):
    ck=request.user.profile.type_ck
    my_info=request.user.profile.my_info

    return render(request,'jq.html',{"ck":ck,"my_info":my_info})



@require_POST
def check(request):
    
    top_3={}
    data=json.loads(request.body)
    top_3=acci_type(data["myinfo"])
   

    return HttpResponse(json.dumps(top_3),content_type="application/json")