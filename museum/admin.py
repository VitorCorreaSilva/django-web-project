from django.contrib import admin
from .models import Construction, Artist, Event

admin.site.register(Artist)
admin.site.register(Construction)
admin.site.register(Event)