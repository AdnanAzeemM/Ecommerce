from django import forms
from .models import ProductReview, ShippingAddress
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = '__all__'

class ShippingAddress(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
