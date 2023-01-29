from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Insert topic is done')
    return render(request,'insert_topic.html')
    

def insert_webpage(request):
        topics=Topic.objects.all()
        d={'topics':topics}
        if request.method=="POST":
            topic=request.POST['topic']
            name=request.POST['name']
            url=request.POST['url']
            T=Topic.objects.get_or_create(topic_name=topic)[0]
            T.save()
            W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
            W.save()
            return HttpResponse('insert webpage is done')
        return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    webpage=Webpage.objects.all()
    d={'webpage':webpage}
    if request.method=="POST":
        name=request.POST['name']
        date=request.POST['date']
        W=Webpage.objects.get_or_create(name=name)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=date)[0]
        A.save()
        return HttpResponse('accessrecords are inserted')
    return render(request,'insert_accessrecord.html',d)