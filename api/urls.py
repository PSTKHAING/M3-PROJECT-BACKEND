from django.urls import path
from api.views import *

urlpatterns = [
    path('category/list/',CategoryList),
    path('category/create/',CategoryCreate),
    path('category/detail/<int:pk>/',CategoryDetail),
    path('category/update/<int:pk>/',CategoryUpdate),
    path('category/delete/<int:pk>/',CategoryDelete),


    path('product/list/',ProductList),
    path('product/create/',ProductCreate),
    path('product/detail/<int:pk>/',ProductDetail),
    path('product/update/<int:pk>/',ProductUpdate),
    path('product/delete/<int:pk>/',ProductDelete),
]