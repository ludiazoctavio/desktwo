from django.contrib import admin

from .models import Ticket, Area, Item

admin.site.register(Ticket)
admin.site.register(Area)
admin.site.register(Item)
