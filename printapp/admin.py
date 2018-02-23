from django.contrib import admin

from .models import Kontrak, Receiving, Ppm, Jabat, HistoryBayar, Termin

# Register your models here.
admin.site.register(Kontrak)
admin.site.register(Receiving)
admin.site.register(Ppm)
admin.site.register(Jabat)
admin.site.register(HistoryBayar)
admin.site.register(Termin)