from django.contrib import admin
from store.models import WinStore, WinStoreExcel, WinStoreUrl, WinRevenue, WinSell


# Register your models here.
class WinStoreAdmin(admin.ModelAdmin):
    list_display = (
        "store_id",
        "user",
        "store_address",
        "store_name",
        "store_reg_num",
        "store_email",
        "store_state",
    )


class WinStoreExcelAdmin(admin.ModelAdmin):
    list_display = ("store_excel_id", "store", "store_excel")


class WinStoreUrlAdmin(admin.ModelAdmin):
    list_display = ("store_url_id", "store", "store_map_url")


class WinRevenueAdmin(admin.ModelAdmin):
    list_display = ("revenue_id", "store", "revenue_value", "revenue_date")


class WinSellAdmin(admin.ModelAdmin):
    list_display = (
        "sell_id",
        "store",
        "wine",
        "sell_reg_time",
        "sell_price",
        "sell_promot",
        "sell_state",
    )


admin.site.register(WinStore, WinStoreAdmin)
admin.site.register(WinStoreExcel, WinStoreExcelAdmin)
admin.site.register(WinStoreUrl, WinStoreUrlAdmin)
admin.site.register(WinRevenue, WinRevenueAdmin)
admin.site.register(WinSell, WinSellAdmin)
