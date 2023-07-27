from django.contrib import admin
from search.models import WinSearch

class WinSearchAdmin( admin.ModelAdmin ):
    list_display = ("search_id", "user_id", "search_word", "search_time" )

admin.site.register( WinSearch, WinSearchAdmin )