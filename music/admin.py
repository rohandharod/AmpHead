from django.contrib import admin
from .models import Song, History, Listenlater, Channel
# Register your models here.

admin.site.register(Song)
admin.site.register(Listenlater)
admin.site.register(History)
admin.site.register(Channel)

