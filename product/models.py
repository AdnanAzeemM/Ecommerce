from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.Company_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=settings.PIC_UP_PATH, blank=True, null=True)
    offer = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    specification = models.ForeignKey('product.ProductSpecification', on_delete=models.CASCADE)
    discount_price = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    trending = models.BooleanField(default=False)
    Slider = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            print('===')
            # This code only happens if the objects is
            # not in the database yet. Otherwise it would
            # have pk
        
        super().save(*args, **kwargs)


class ProductSpecification(models.Model):
    capacity = models.CharField(max_length=255)
    weight_dimensions = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    chip = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    video_recording = models.CharField(max_length=255)

    def __str__(self):
        return self.display


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to=settings.PIC_UP_PATH, blank=True, null=True)



class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    review = models.TextField(blank=True)
    rating = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)


class CheckoutCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    comp_name = models.CharField(max_length=255, null=True, blank=True)
    area_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    busines_address = models.BooleanField(default=False ,null=True, blank=True)

    
class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, 
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username