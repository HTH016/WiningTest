from errorhandling import views
from django.urls.conf import path

urlpatterns = [
    path("purchaseerrorpage", views.PurchaseErrorView.as_view(), name="purchaseError"),
    path("storeerrorpage", views.StoreErrorView.as_view(), name="storeError"),
]
