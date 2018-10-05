# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib import admin
from accounts.models import Ideator
from django.db.models.signals import post_save

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Ideas(models.Model):
    ideator=models.ForeignKey(Ideator,on_delete=models.CASCADE)
    username=models.CharField(max_length=20,blank=True)
    subject=models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=3000,blank=False,default="description")
    expectation= models.CharField(max_length=2000,blank=True,default="lkdjkfjskldfkjklsd lksdfkjjskdf lksdfjkjf")
    Is_patent=models.BooleanField(default=False)
    #domain_ = ArrayField(models.CharField(max_length=200), blank=True)

        


    def create_idea(sender , instance, **kwargs):
              if(instance):
                  idea_details=Ideas.objects.create(username=instance.username)
    post_save.connect(create_idea,sender=Ideator)
