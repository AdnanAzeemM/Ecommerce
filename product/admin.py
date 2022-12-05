from django.contrib import admin
from .models import Category, Product, Company, ProductSpecification, ProductImages, ProductReview, CheckoutCart, ShippingAddress


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'Company_name']


@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'img', 'offer',
                    'specification', 'discount_price', 'price', 'trending', 'Slider']


@admin.register(ProductSpecification)
class Product_Specification_Admin(admin.ModelAdmin):
    list_display = ['id', 'capacity', 'weight_dimensions', 'display', 'chip', 'camera',
                    'video_recording']


@admin.register(ProductImages)
class ProductImg_Admin(admin.ModelAdmin):
    list_display = ['id', 'product', 'product_img']


@admin.register(ProductReview)
class ProductReview_Admin(admin.ModelAdmin):
    list_display = ['id', 'product', 'name', 'title', 'review', 'rating', 'date']


@admin.register(CheckoutCart)
class CheckoutCart_Admin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'created_at']


@admin.register(ShippingAddress)
class ShippingAddress_Admin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'first_name', 'last_name', 'comp_name', 'area_code', 'phone', 'address', 'zip_code', 'busines_address']