from django.db import models
from django import forms

class Post(models.Model):
    title = models.CharField(max_length = 140)
    url = models.CharField(max_length = 300)
    date = models.DateTimeField()
    body = models.TextField()
    tags = models.CharField(max_length = 140)

    USEFUL = 'US'
    SUPPORT = 'SP'
    TRAINING = 'TR'
    API = 'AP'
    SDK = 'SD'
    ROADMAP = 'RM'
    JIRA = 'JR'
    PROCESSES = 'PR'
    USECASE = 'UC'

    list_of_choices = (
            (USEFUL, 'Useful Links'),
            (SUPPORT, 'Platform Support'),
            (TRAINING, 'Training Materials'),
            (API, 'API Documentation'),
            (SDK, 'Mobile SDK\'s'),
            (ROADMAP, 'Map Versions/Roadmaps'),
            (JIRA, 'Jira Systems'),
            (PROCESSES, 'Processes'),
            (USECASE, 'Use-Cases'),
        )
    
    categories = models.CharField(max_length=2,
                                  choices=list_of_choices,
                                  default=USEFUL)
    
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(
        max_length=50
        )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0
        )
