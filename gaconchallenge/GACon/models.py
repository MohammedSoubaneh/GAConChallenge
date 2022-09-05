from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    bio = models.TextField()

class Talks(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField()
    room = models.IntegerField()
    speaker = models.ManyToManyField(Speaker)

class Attendees(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    registered = models.DateTimeField(auto_now_add=True)

class Event(BaseModel):
    talks = models.ForeignKey(Talks, on_delete=models.CASCADE)
    attendees = models.ForeignKey(Attendees, on_delete=models.CASCADE)
