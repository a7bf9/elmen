from django.contrib import admin

from .models import List, Link, Entry

admin.site.register(List)
admin.site.register(Link)
admin.site.register(Entry)