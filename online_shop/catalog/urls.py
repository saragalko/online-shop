from django.urls import path
from catalog.views import (CategoryListView, CategoryProductsView, DiscountListView, DiscountProductsView,
                           SellerListView, SellerProductsView)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),
    path('discounts/', DiscountListView.as_view()),
    path('discounts/<int:discount_id>/', DiscountProductsView.as_view()),
    path('sellers/', SellerListView.as_view()),
    path('sellers/<int:seller_id>/', SellerProductsView.as_view()),
]
