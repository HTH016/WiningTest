from django.contrib import admin
from search.models import WinSearch, WinSearchN


class WinSearchAdmin(admin.ModelAdmin):
    list_display = ("search_id", "user_id", "search_word", "search_time")


admin.site.register(WinSearch, WinSearchAdmin)


class WinSearchNAdmin(admin.ModelAdmin):
    list_display = ("search_n_id", "search_n_word", "search_n_time")


admin.site.register(WinSearchN, WinSearchNAdmin)
