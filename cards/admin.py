from django.contrib import admin

# Register your models here.
from .models import Card, Album, Sport, Wish, About

admin.site.register(Card)
admin.site.register(Album)
admin.site.register(Sport)
admin.site.register(Wish)
admin.site.register(About)