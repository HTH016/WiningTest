from django.urls.conf import path
from board import views


from django.conf import settings
from django.conf.urls.static import static

app_name = "board"

urlpatterns = [  # init_url == "http://localhost:8000/board/list"
    path("list", views.ListView.as_view(), name="list"),
    path("list/", views.ListView.as_view(), name="board_list"),
    path("write", views.WriteView.as_view(), name="write"),
    path(
        "deletecomment/<int:comment_id>/",
        views.DeleteCommentView.as_view(),
        name="deletecomment",
    ),
    path("writecomment/", views.WriteCommentView.as_view(), name="writecomment"),
    path("content", views.ContentView.as_view(), name="content"),
    path("content/<int:board_id>/", views.ContentView.as_view(), name="content"),
    #    path("content/", views.ContentView.as_view(), name="content"),
    #    path("contentpro", views.ContentProView.as_view(), name="contentpro"),
    path("delete", views.DeleteView.as_view(), name="delete"),
    path("update", views.UpdateView.as_view(), name="update"),
    path("updatepro", views.UpdateProView.as_view(), name="updatepro"),
    path("board/content/", views.ContentView.as_view(), name="content"),
    # path('board/toggle_like/', views.ContentView.as_view().toggle_like, name='toggle_like'),
    #    path("content/", views.ContentView.as_view(), name="content"),
    #    path("contentpro", views.ContentProView.as_view(), name="contentpro"),
    #    path("image", views.ImageView.as_view(), name="image"),
    #    path("imagedown", views.ImageDownView.as_view(), name="imagedown"),
    path("uploadimage", views.UploadImageView.as_view(), name="uploadimage"),
	path('updatecomment/', views.UpdateCommentView.as_view(), name="updatecomment") 
]
urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_URL
)  # MEDIA 경로 추가
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # MEDIA 경로 추가
