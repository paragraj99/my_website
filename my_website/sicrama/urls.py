from unicodedata import name
from . import views
from django.urls import path,include

urlpatterns = [
    path('product',views.product,name='product'),
    path('product_list',views.product_list,name='product_list'),
    path('delete/<id>',views.delete,name='delete'),
    path('add_product',views.add_product,name='add_product'),
    path('add',views.add,name="add"),
    path('edit/<id>',views.edit,name='edit'),
    path('update', views.update, name='update'),
]