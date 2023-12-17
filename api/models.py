from django.contrib.auth.models import User, AbstractUser, Permission
from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = 'username'



class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='members')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
class List(models.Model):
    name = models.CharField(max_length=255, default="liste non nommée")
    board = models.ForeignKey(Board, default="test", null=False, on_delete=models.CASCADE, related_name='lists')
    datetime = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    list = models.ForeignKey(List, null=False, related_name='cards', on_delete=models.CASCADE)
    importance = models.IntegerField(default=0, blank=True, null=True, validators=[MaxValueValidator(10)])
    datetime = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


