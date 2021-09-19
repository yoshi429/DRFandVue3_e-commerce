from django.urls import path

from .views import (
    CategoryDetail, LatestProductList, ProductDetail,
    search
)

urlpatterns = [
    path('latest-products/', LatestProductList.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
] 
