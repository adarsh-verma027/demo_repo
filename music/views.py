from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader



# Create your views here.

def index(request):
    all_album = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_album

    }
    #html = ''
    #for album in all_album:
     #   url = '/music/'+str(album.id)+'/'
     #   html += '<a href="'+url+'">'+album.album_title+'</a><br>'
    return  HttpResponse(template.render(context, request))

def detail(request, album_id):
        return HttpResponse('<h2>Details for album:'+str(album_id)+"</h2>")