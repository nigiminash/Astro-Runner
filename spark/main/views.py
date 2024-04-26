from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import News
from .models import Jobs

def index11(request):
    latest_nid = News.objects.all().values_list('id', flat=True).order_by('-id').first()
    latest_n = News.objects.filter(id = latest_nid).values()
    latest_jid = Jobs.objects.all().values_list('id', flat=True).order_by('-id').first()
    latest_j = Jobs.objects.filter(id = latest_jid).values()
    context = {"ln": latest_n, "lj": latest_j}
    template = loader.get_template("main/ARhome.html")
    return HttpResponse(template.render(context, request))

def index00(request):
    nachricht = reversed(News.objects.all().values())
    template = loader.get_template("main/ARnews.html")
    context = {"nachricht": nachricht,}
    return HttpResponse(template.render(context, request))

def index22(request):
    job = reversed(Jobs.objects.all().values())
    template = loader.get_template("main/ARcareer.html")
    context = {"job": job,}
    return HttpResponse(template.render(context, request))

def index33(request):
    context = None
    template = loader.get_template("main/ARaboutus.html")
    return HttpResponse(template.render(context, request))

def index44(request):
    context = None
    template = loader.get_template("main/ARtickets.html")
    return HttpResponse(template.render(context, request))

'''
def index1(request):
    allusers = User.objects.all().values()
    template = loader.get_template("main/base.html")
    context = {"allusers" : allusers,}
    return HttpResponse(template.render(context, request))

    def __str__(self):
        return f"{self.vorname} {self.nachname}"

def index1_details(request, id):
    chosenuser = User.objects.get(id = id)
    template = loader.get_template("main/user_details.html")
    context = {"chosenuser" : chosenuser,}
    return HttpResponse(template.render(context, request))

'''