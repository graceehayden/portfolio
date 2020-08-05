def handle_uploaded_file(file):
    file_address = 'sounds/' + file + '.mp3'
    with open(file_address, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        audio = MP3(song_address)
        c = Song(title = song_title, songfile = song_address)
        c.save()

def songs(request):
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            song_title = request.POST.get('song_title')
            file = request.POST.get('songfile')
            song_address = 'sounds/' + file + '.mp3'
            with open(song_address, 'wb+' ) as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
                audio = MP3(song_address)
                c = Song(title = song_title, songfile = song_address)
                c.save()
            return redirect('playlist')
    else:
        form = SongUploadForm()
    return render(request, 'songs.html', {'form': form})
