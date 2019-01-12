from django.db import models
import uuid

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cards')
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    link = models.URLField(max_length=1000)
    time_stamp = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Sport(models.Model):
    sport = models.CharField(max_length=400)

    def __str__(self):
        return self.sport

class Album(models.Model):
    album = models.CharField(max_length=400)

    def __str__(self):
        return self.album

class Wish(models.Model):
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return str(self.id)

class About(models.Model):
    about = models.TextField()

    def __str__(self):
        return 'about'