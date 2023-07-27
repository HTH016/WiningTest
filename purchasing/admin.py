from django.contrib import admin
from purchasing.models import (
    WinPurchase,
    WinPurchaseDetail,
    WinCart,
    WinCartDetail,
    WinReceiveCode,
)


# Register your models here.
class WinPurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "purchase_id",
        "user",
        "purchase_time",
        "purchase_number",
        "purchase_price",
    )


class WinPurchaseDetailAdmin(admin.ModelAdmin):
    list_display = (
        "purchase_detail_id",
        "purchase",
        "sell",
        "purchase_det_number",
        "purchase_det_price",
        "purchase_det_state",
    )


class WinCartAdmin(admin.ModelAdmin):
    list_display = ("cart_id", "user", "cart_time", "cart_state")


class WinCartDetailAdmin(admin.ModelAdmin):
    list_display = ("cart_det_id", "sell", "cart", "cart_det_qnty")


class WinReceiveCodeAdmin(admin.ModelAdmin):
    list_display = ("receive_code_id", "purchase_detail_id", "receive_code")


admin.site.register(WinPurchase, WinPurchaseAdmin)
admin.site.register(WinPurchaseDetail, WinPurchaseDetailAdmin)
admin.site.register(WinCart, WinCartAdmin)
admin.site.register(WinCartDetail, WinCartDetailAdmin)
admin.site.register(WinReceiveCode, WinReceiveCodeAdmin)
