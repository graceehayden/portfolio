from django.forms import ModelForm
from .models import *


class SongUploadForm(ModelForm):
    class Meta:
        model = Song
        fields = ["title", "songfile"]
