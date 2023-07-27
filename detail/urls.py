from django.urls.conf import path
from detail import views

app_name = "detail"
urlpatterns = [
    path("winedetail", views.WineDetailInfoView.as_view(), name="winedetail"),
]
