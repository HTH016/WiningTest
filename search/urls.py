from django.urls.conf import path
from search import views

app_name = "search"
urlpatterns = [  # init_url == "http://localhost:8000/search/main"
    path("main", views.SearchByNameView.as_view(), name="main"),
    path("searchbynamelist", views.SearchByNameView.as_view(), name="searchbynamelist"),
    path(
        "searchbycategory",
        views.SearchByCategoryView.as_view(),
        name="searchbycategory",
    ),
    path(
        "searchbycategorylist",
        views.SearchByCategoryView.as_view(),
        name="searchbycategorylist",
    ),
    path("searchbyuser", views.SearchByUserView.as_view(), name="searchbycategorylist"),
    path(
        "searchbyuserlist",
        views.SearchByUserView.as_view(),
        name="searchbycategorylist",
    ),
    path("searchbyrank", views.SearchByRankView.as_view(), name="searchbycategorylist"),
    path(
        "searchbyranklist",
        views.SearchByRankView.as_view(),
        name="searchbycategorylist",
    ),
]
