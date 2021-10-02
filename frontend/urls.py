from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('category-product/<int:product_category_id>', views.CategoryProducts, name= "CategoryProducts" ),
]