from django.contrib import admin
from detail.models import WinDetailView, WinDetailViewN, WinWine, WinWineRegion


class WinDetailViewAdmin(admin.ModelAdmin):
    list_display = ("detail_view_id", "user_id", "wine_id", "detail_view_time")


admin.site.register(WinDetailView, WinDetailViewAdmin)


class WinDetailViewNAdmin(admin.ModelAdmin):
    list_display = ("detail_view_n_id", "wine_id", "detail_view_n_time")


admin.site.register(WinDetailViewN, WinDetailViewNAdmin)


class WinWineAdmin(admin.ModelAdmin):
    list_display = (
        "wine_id",
        "wine_name",
        "wine_name_eng",
        "wine_sort",
        "wine_capacity",
        "wine_alc",
        "wine_dangdo",
        "wine_sando",
        "wine_tannin",
        "wine_food",
        "wine_image",
        "wine_region_id",
    )


admin.site.register(WinWine, WinWineAdmin)


class WinWineRegionAdmin(admin.ModelAdmin):
    list_display = ("wine_region_id", "wine_region_name")


admin.site.register(WinWineRegion, WinWineRegionAdmin)
