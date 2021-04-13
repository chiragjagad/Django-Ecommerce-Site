from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('fashion/', views.fashion, name="fashion"),
    path('books/', views.books, name="books"),
    path('electronics/', views.electronics, name="electronics"),
    path('accessories/', views.accessories, name="accessories"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]