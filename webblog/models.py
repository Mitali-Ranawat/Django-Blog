from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Blog Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name) + ' | ' + self.profession


