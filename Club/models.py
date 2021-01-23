from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    title = models.CharField(max_length = 255)
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    adjenda = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Meeting'
        verbose_name_plural = 'Meetings'


class Meeting_Minutes(models.Model):
    meetID = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField()

    def __str__(self):
        return self.meetID

    class Meta:
        db_table = 'Meeting Minutes'
        verbose_name_plural = 'Meeting Minutes'
        


class Resource(models.Model):
    resname = models.CharField(max_length = 255)
    restype = models.TextField()
    URL = models.URLField()
    date_entered = models.DateField()
    userID = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.resname
    
    class Meta:
        db_table = 'Resource'
        verbose_name_plural = 'Resources'


class Event(models.Model):
    title = models.CharField(max_length = 255)
    location = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Event'
        verbose_name_plural = 'Events' 
    


# Create your models here.
