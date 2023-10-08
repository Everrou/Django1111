from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    numKino = Kino.objects.all().count()
    numActor = Actor.objects.all().count()
    numFree = Kino.objects.filter(status__kino=1).count()
    data = {'k1':numKino,'k2':numActor,'k3':numFree}

    return render(req,'index.html',context=data)

#def allkino(req):
#    return render(req,'index.html')
from django.views import generic
class kinolist123(generic.ListView):
    model = Kino

class kinoDetail(generic.DetailView):
    model = Kino


#from django.http import HttpResponse
#def info(req,id):
 #   film = Kino.objects.get(id=id)
 #   return HttpResponse(film.title)
