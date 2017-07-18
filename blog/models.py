from django.db import models
from django.utils import timezone


class Post(models.Model): #Class indicates that we are defining an object, Post is the name of our model, and models.Model means that the Post is a Django Model
    author = models.ForeignKey('auth.User') #link to another model
    title = models.CharField(max_length=200) #how you define a text with a limited number of characters
    text = models.TextField() #for long text without a limit
    created_date = models.DateTimeField(
            default=timezone.now) #this is a date and time
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #def means this is a function/method and publish is the name of the method
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #method will return something
        return self.title
