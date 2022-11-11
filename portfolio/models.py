from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone


# class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    middle_name = models.CharField(max_length=30, blank=True)
#    dob = models.DateField(null=True, blank=True)


class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return str(self.videofile)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
