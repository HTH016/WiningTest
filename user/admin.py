from django.contrib import admin
from user.models import WinUser, WinUserFavorite, WinUserGrade, WinPointHis, WinReview


class WinUserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "user_grade",
        "user_passwd",
        "user_name",
        "user_email",
        "user_tel",
        "user_reg_date",
        "user_point",
    )


admin.site.register(WinUser, WinUserAdmin)


class WinUserFavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "fav_user_id",
        "user_id",
        "fav_wine_color",
        "fav_alc",
        "fav_numbwith",
        "fav_sweet",
        "fav_bitter",
        "fav_sour",
        "fav_season",
        "fav_food",
    )


admin.site.register(WinUserFavorite, WinUserFavoriteAdmin)


class WinUserGradeAdmin(admin.ModelAdmin):
    list_display = ("user_grade", "user_grade_name")


admin.site.register(WinUserGrade, WinUserGradeAdmin)


class WinPointHisAdmin(admin.ModelAdmin):
    list_display = ("point_his_id", "user_id", "point_reg", "point_add")


admin.site.register(WinPointHis, WinPointHisAdmin)


class WinReviewAdmin(admin.ModelAdmin):
    list_display = (
        "review_id",
        "user_id",
        "sell_id",
        "review_content",
        "review_score",
        "review_reg_time",
    )


admin.site.register(WinReview, WinReviewAdmin)
