from cgi import test
from cgitb import text
from multiprocessing import AuthenticationError
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True) # blank=True means it's ok for the post's body to be empty
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ties the User who logs in as the Author. 
        # Django already has a db table for users, so it's just imported.
        # Author is a foreign key field to User.
        # the on_delete part tells Django to delete posts of any User that gets deleted.
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True) # allowing null is how we can tell it hasn't been published yet
        # it's how we're going to say whether or not it should be viewable publicly.
    # in my attempt I only had DateField, not DateTimeField, I'm assuming adding the time puts the timestamp in addition to date stamp...


    def __str__(self):
        return self.title

class Category(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'     