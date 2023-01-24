from django.shortcuts import render
from app1.models import *
# Create your views here.
def display_topic(request):
    QST=Topic.objects.all()
    d={'topic':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QST=Webpages.objects.all()
    d={'webpages':QST}
    return render(request,'display_webpage.html',d)


def display_accessrecords(request):
    QST=AccessRecords.objects.all()
    d={'accessrecords':QST}
    return render(request,'display_accessrecords.html',d)