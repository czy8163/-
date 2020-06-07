from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader,RequestContext
from chengji.models import chengji

# Create your views here.
def sy(request):
    return render(request,'chengji/首页.html')

def login_check(request):
    name=request.POST.get('name')
    zcz=chengji.objects.all()
    for i in zcz:
        if name==i.bId:
            goal=i.bgoal
            return render(request,'chengji/成绩.html',{'name':i.bname,'ID':i.bId,'goal':goal})
        else:
            continue
    return redirect('/deng')