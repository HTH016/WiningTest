from django.urls.conf import path
from store import views

urlpatterns = [
    path(
        "store-registration",
        views.StoreRegistrationView.as_view(),
        name="storeRegistration",
    ),
    path(
        "check-reqnum",
        views.CheckStoreRegistNumberView.as_view(),
        name="checkRegistNumber",
    ),
    path(
        "product-addition", views.ProductAdditionView.as_view(), name="productAddition"
    ),
    path("store-mypage", views.StoreMyPageView.as_view(), name="storeMyPage"),
    path("search-product", views.SearchProduct.as_view(), name="searchProduct"),
    path("store-info", views.StoreInfoView.as_view(), name="storeInfo"),
    path(
        "search-receive-code",
        views.SearchReceiveCodeView.as_view(),
        name="searchReceiveCode",
    ),
    path(
        "store-info-modification",
        views.StoreInfoModificationView.as_view(),
        name="storeInfoModification",
    ),
    path("sell-detail-list", views.SellDetailListView.as_view(), name="sellList"),
    path("product-list", views.ProductListView.as_view(), name="productList"),
    path(
        "discontinue-product",
        views.DiscontinueProductView.as_view(),
        name="discontinueProduct",
    ),
    path("drop-store", views.DropStoreView.as_view(), name="dropStore"),
    path("store-revenue", views.StoreRevenueMainView.as_view(), name="storeRevenue"),
    path("store-revenue-term", views.StoreRevenueTermView.as_view()),
]
