from django.db import models

# Create your models here.

LANGUAGE_CHOICES = (
    {'AR', 'Arabic'},
    {'EN', 'English'}
)

GENDER_CHOICES = (
    {'F', 'Female'},
    {'M', 'Male'}
)

LIKES_CHOICES = (
    {'H', 'Heart'},
    {'L', 'Like'},
    {'J', 'Joyful'},
    {'H', 'Haha'},
)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    short_bio = models.TextField(max_length=250)
    profile_picture = models.ImageField(upload_to='photos')
    email = models.EmailField (max_length=254)
    # country = models.models.CharField( max_length=50)
    language = models.CharField(choices= LANGUAGE_CHOICES, max_length=50)
    creation_date = models.DateField()

    def __str__(self):
        return self.first_name


class Pin(models.Model):
    title = models.CharField(max_length=50)
    alternative_desc  = models.CharField(max_length=100)
    pin_picture = models.ImageField(upload_to='photos')
    destination_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title 


class Board(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=50)
    content  = models.TextField(max_length=500)
    content_picture = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.title 


class Notification(models.Model):
    content  = models.TextField(max_length=500)
    creation_date = models.DateField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.creation_date


class Comment(models.Model):
    content  = models.TextField(max_length=500)

    def __str__(self):
        return self.content

class Like(models.Model):
    type  = models.CharField(max_length=500)

    def __str__(self):
        return self.type

    
        






