from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def index(req):
    numKino = Kino.objects.all().count()
    numActor = Actor.objects.all().count()
    numFree = Kino.objects.filter(status__kino=1).count()
    if req.user.username:
        username = req.user.first_name
        print(req.user.first_name, '#', req.user.id)
    else:
        username = 'Гость'
        print(req.user.id)
    data = {'k1':numKino,'k2':numActor,'k3':numFree,'username':username}
    #user = User.objects.create_user('user2','user2@mail.ru','useruser')
   # user.first_name = 'Vlad'
    #user.last_name = 'Petrov'
    #user.save()
    return render(req,'index.html',context=data)

#def allkino(req):
#    return render(req,'index.html')
from django.views import generic
class kinolist123(generic.ListView):
    model = Kino
    paginate_by = 2

class kinoDetail(generic.DetailView):
    model = Kino

class Actorlist(generic.ListView):
    model = Actor
    paginate_by = 50


class ActorDetail(generic.DetailView):
    model = Actor


class Directorlist(generic.ListView):
    model = Director
    paginate_by = 50


class DirectorDetail(generic.DetailView):
    model = Director

#from django.http import HttpResponse
#def info(req,id):
 #   film = Kino.objects.get(id=id)
 #   return HttpResponse(film.title).

def status(req):
    k1 = Status.objects.all()
    data = {'podpiska':k1}
    return render(req,'podpiska.html',context=data)

def prosmotr(req, id1, id2, id3):
    print(id1, id2, id3)
    mas = ['бесплатно', 'базовая', 'супер']  # kino id2
    mas2 = ['Free', 'Based', 'Super']  # user id3
    podp = User.objects.get(id=id3).groups.all()[0].id
    print(podp)
    if id3 == 0:
        podp = 1
    if podp >= id2:
        print('can watch')
    else:
        print('can\'t watch')
    return render(req, 'index.html')
