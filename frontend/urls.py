from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('login',views.customerLogin, name="customerLogin"),
    path('product/<int:product_id>', views.ProductDetails, name="ProductDetails"),
    path('category-product/<int:product_category_id>', views.CategoryProducts, name= "CategoryProducts" ),
]