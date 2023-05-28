from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.urls import reverse

# Create your models here.


class AdPost(models.Model):
    ADPOST_TYPE = [
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('byers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('poitioner', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    ]
    title = models.CharField(max_length=256, unique=True)
    text = models.TextField()
    adpost_type = models.CharField(max_length=16, choices=ADPOST_TYPE, default='tank')
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    adpost = models.ForeignKey(AdPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
