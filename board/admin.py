from django.contrib import admin
from board.models import WinBoard, WinBoardImg, WinComment


class WinBoardAdmin(admin.ModelAdmin):
    list_display = (
        "board_id",
        "user_id",
        "board_title",
        "board_reg_time",
        "board_content",
        "board_read_count",
        "board_ip",
    )


admin.site.register(WinBoard, WinBoardAdmin)
# admin.site.register(Comment)


class WinBoardImgAdmin(admin.ModelAdmin):
    list_display = ("board_img_id", "board_id", "board_image")


admin.site.register(WinBoardImg, WinBoardImgAdmin)


class WinCommentAdmin(admin.ModelAdmin):
    list_display = (
        "comment_id",
        "board_id",
        "user_id",
        "comment_content",
        "comment_reg_time",
        "content_ip",
    )


admin.site.register(WinComment, WinCommentAdmin)
