from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title


class Employ(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    info = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


class Company(models.Model):
    pass
