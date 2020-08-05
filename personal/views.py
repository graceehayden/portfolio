from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from django.utils import timezone
from django.template import RequestContext
from .forms import *
from .models import *
from .functions import handle_uploaded_file
import random


AUDIO_FILE_TYPES = ['mp3', 'wav']


def home(request):
    ''' Home page '''
    return render(request, 'home.html', {})


def inspiration_station(request):
    return render(request, 'home.html', {})


def travel_inspiration(request):
    return render(request, 'travel_inspiration.html', {})


def post_list(request):
    posts = Post.objects.order_by('published_date')[:3]
    return render(request, 'function_junction.html', {'posts': posts})


def upload_song(request):
    form = SongUploadForm()
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.songfile = request.FILES['songfile']
            file_type = song.songfile.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in AUDIO_FILE_TYPES:
                messages.error(request, "You cannot upload a song with that file type.")
                return render(request, 'upload_song.html')
            song.save()
            messages.success(request, "Song successfully uploaded.")
            
    context = {"form": form,}
    return render(request, 'upload_song.html', context)


def playlist(request):
    songs = Song.objects.all()
    #Song.objects.get(title="A SONG").delete()
    songs_dict = {}
    for song in songs:
        title = song.title
        file = song.songfile
        songs_dict.update( {title : file.url} )
    print(songs_dict)
    return render(request, 'playlist.html', {'songs': songs_dict })


def videos(request):
    request.session['page'] = 'videos'
    if not request.user.is_active:
        return redirect('user_login')
    else:
        form= VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        videos = []
        videos = Video.objects.all()
        print(videos)
        context= {
                  'videos': videos,
                  'form': form
                  }
        return render(request, 'videos.html', context)


def hello_pallet(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'hello_pallet.html', {'posts': posts})
