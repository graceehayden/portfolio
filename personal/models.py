from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    songfile = models.FileField(upload_to="sounds/")
    duration = models.FloatField(null=True, blank=True)
    isPlaying = False

    def __str__(self):
        return self.title
