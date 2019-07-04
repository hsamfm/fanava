from django.urls import path

from .views import *

urlpatterns = [
    path('', StoreView.as_view(), name="index"),
    path('category/<name>/', StoreDetail.as_view(), name="category-detail")
]
