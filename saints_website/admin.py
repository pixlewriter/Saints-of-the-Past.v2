from django.contrib import admin

from saints_website.models import Saint, Entry, Prayer

admin.site.register(Saint)
admin.site.register(Entry)
admin.site.register(Prayer)

