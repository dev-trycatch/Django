from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/update/<int:id>/', views.category_update, name='category_update'),
    path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),

    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/update/<int:id>/', views.product_update, name='product_update'),
    path('products/delete/<int:id>/', views.product_delete, name='product_delete'),
]
