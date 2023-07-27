from django.urls.conf import path
from user import views

urlpatterns = [  # init_url == "http://localhost:8000/user/login"
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("inputUser", views.InputUserView.as_view(), name="inputUser"),
    path("inputStore", views.InputStoreView.as_view(), name="inputStore"),
    path("confirmId", views.ConfirmIdView.as_view(), name="confirmId"),
    path("delete", views.DeleteView.as_view(), name="delete"),
    path("myPage", views.MyPageView.as_view(), name="myPage"),
    path("modifyUser", views.ModifyUserView.as_view(), name="modifyUser"),
    path("reviewWrite", views.ReviewWriteView.as_view(), name="reviewWrite"),
    path("reviewList", views.ReviewListView.as_view(), name="reviewList"),
    path("purchaseDetail", views.PurchaseDetailView.as_view(), name="purchaseDetail"),
    path("myBoard", views.MyBoardView.as_view(), name="myBoard"),
    path("addPoint", views.AddPointView.as_view(), name="addPoint"),
    path("addPointHis", views.AddPointHisView.as_view(), name="addPointHis"),
    path("myComment", views.MyCommentView.as_view(), name="myComment"),
]
