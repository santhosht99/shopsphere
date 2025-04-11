from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path('login_page',views.login_page,name="login_page"),
    path('signout', views.signout, name='signout'),
    path('main',views.main,name="main"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart',views.cart_view,name='cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('payment',views.payment_page,name="payment"),
    path('order-success/', views.confirm_order, name='success'),


]
