from django.shortcuts import render
from product import models as ProductModels
from cart import models as CartModels
import product

def homePage(request):
    
    """ Fetch latest data in acending order by id """ 
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    productCategories = ProductModels.ProductCategory.objects.filter(status = True)
    products = ProductModels.Product.objects.filter(status=True).order_by('-id')[:3]
    
    return render(request, 'index.html',{
        'navigationProductCategories' : navigationProductCategories,
        'productCategories' : productCategories,
        'products' : products 
    })

def CategoryProducts(request, product_category_id):
    """ Product list according to category"""
    navigationProductCategories = ProductModels.ProductCategory.objects.filter(status=True).order_by('-id')[:4]
    product = ProductModels.Product.objects.filter(product_category_id = product_category_id)
    return render(request, 'category-product.html',{
        'navigationProductCategories' : navigationProductCategories
    })