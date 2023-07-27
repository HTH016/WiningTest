from django.contrib import admin
from detail.models import WinDetailView, WinWine, WinWineRegion
from user.models import WinUser

class WinDetailViewAdmin( admin.ModelAdmin ):
    list_display = ( "detail_view_id", "user", "wine", "detail_view_time" )

admin.site.register( WinDetailView, WinDetailViewAdmin )

class WinWineAdmin( admin.ModelAdmin ):
    list_display = ( "wine_id", "wine_name", "wine_name_eng", "wine_sort", "wine_capacity", "wine_alc", 
                     "wine_dangdo", "wind_sando", "wine_tannin", "wine_food", "wine_image", "wine_region")

admin.site.register(  WinWine,  WinWineAdmin )

class WinWineRegionAdmin( admin.ModelAdmin ):
    list_display = ("wine_region_id", "wine_region" )

admin.site.register( WinWineRegion, WinWineRegionAdmin )