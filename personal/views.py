from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import *
from .models import *


AUDIO_FILE_TYPES = ['mp3', 'wav']


class Home(TemplateView):
    template_name = 'home.html'


###################################


def post_list(request):
    posts = Post.objects.order_by('published_date')[:3]
    return render(request, 'function_junction.html', {'posts': posts})

# class UploadSong(View):
#     def get(self, request, pk):
#         task = Task.objects.get(id=pk)
#         context = {'task':task}
#         return render(request, 'base/delete.html', context)
#
#     def post(self, request, pk):
#         task = Task.objects.get(id=pk)
#         task.delete()
#         return redirect('tasks')


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

    songs_delete = []
    songs_dict = {}
    for song in songs:
        title = song.title
        file = song.songfile
        songs_dict.update( {title : file.url} )
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
        context= {
                  'videos': videos,
                  'form': form
                  }
        return render(request, 'videos.html', context)


def hello_pallet(request):
    return render(request, 'hello_pallet.html')
