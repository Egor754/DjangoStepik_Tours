from django.contrib import admin

from .models import Tours, Depart


class ToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'date', 'departure')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'country', 'date')


class DepartureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ru_departure')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Tours, ToursAdmin)
admin.site.register(Depart, DepartureAdmin)
