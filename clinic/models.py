from django.db import models
from django.contrib.auth.models import User
from sklearn.ensemble import RandomForestClassifier
import joblib
from django import forms
from django.contrib import admin
import random
import string




# Create your models here.
SEX = [
    (1, 'Me'),
    (0, 'Ke'),
]

SYMP_1 = [
    (1, 'Kidonda sehemu za siri'),
    (0, 'Hakuna dalili'),
]
SYMP_2 = [
    (1, 'Kutoa uchafu sehemu za siri'),
    (0, 'Hakuna dalili'),
]
SYMP_3 = [
    (1, 'Maumivu tumbo la chini'),
    (0, 'Hakuna dalili'),
]
SYMP_4 = [
    (1, 'Kuwashwa sehemu za siri'),
    (0, 'Hakuna dalili'),
]
SYMP_5 = [
    (1, 'Maumivu wakati au baada ya kukojoa'),
    (0, 'Hakuna dalili'),
]

def generate_random_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=9)) 

class Task(models.Model):
    jina_la_mtumiaji = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    jina_la_kwanza = models.CharField(max_length=200)
    jina_la_pili = models.CharField(max_length=200)
    simu = models.CharField(max_length=200)
    anwani = models.TextField(null=True, blank=True)
    jinsia = models.PositiveIntegerField(choices=SEX)
    umri = models.PositiveIntegerField(null=True, blank=True)
    Namba_ya_mgonjwa = models.CharField(max_length=9, default=generate_random_code, db_index=True, editable = False)
    DALILI1 = models.PositiveIntegerField(choices=SYMP_1)
    DALILI2 = models.PositiveIntegerField(choices=SYMP_2)
    DALILI3 = models.PositiveIntegerField(choices=SYMP_3)
    DALILI4 = models.PositiveIntegerField(choices=SYMP_4)
    DALILI5 = models.PositiveIntegerField(choices=SYMP_5)
    MAAMBUKIZI = models.CharField(max_length=100, blank=True, editable = False)
    complete = models.BooleanField(default=False, editable = False)
    created = models.DateTimeField(auto_now_add=True)
    
    readonly_fields = ('Patient_Id', 'MAAMBUKIZI')
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/model.joblib')
        self.MAAMBUKIZI = ml_model.predict([[self.DALILI1, self.DALILI2, self.DALILI3, self.DALILI4, self.DALILI5]])
        return super().save(*args, *kwargs)
    
    def __str__(self):
        return self.firstname
    
    class Meta:
        ordering = ['complete']
        
             
hosp = [
    (1, 'Tengeru'),
    (2, 'Selian'),
    (3, 'NSK'),
    (4, 'St. Elizabeth'),
    (5, 'AICC'),
    (6, 'Mount Meru'),
    (7, 'St. Joseph'),
]