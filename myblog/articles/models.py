'''
Article module
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        """[Title string function object]
        Returns:
            [str] -- [title]
        """
        return self.title

    def snippet(self):
        """[Function to reduce the size of the body text]
        Returns:
            [textField] -- [body text]
        """
        return self.body[:50] + '...'
