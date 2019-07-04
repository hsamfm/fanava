from django.urls import path

from .views import *

urlpatterns = [
    path('', StoreView.as_view(), name="store-index"),
    path('product/<int:id>/', StoreDetail.as_view(), name="store-detail")
]
