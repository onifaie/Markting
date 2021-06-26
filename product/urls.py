from django.contrib import admin
from django.urls import path
from product.views import Test_list,Detail_product,product_form

urlpatterns = [
    path('',Test_list.as_view(),name='Test_list' ),
    path('Detail_product/<int:pk>/',Detail_product.as_view(),name='Detail_product' ),
    path('product_form/',product_form.as_view(),name='product_form' ),
]
