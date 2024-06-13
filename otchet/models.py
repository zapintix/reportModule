from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class UserAut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessToken = models.CharField(max_length=500)
    refreshToken = models.CharField(max_length=300)

    def __str__(self):
        return self.refreshToken


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Object(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.id


class Report(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


