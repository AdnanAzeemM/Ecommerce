from django.shortcuts import render
from product.models import Category, Product, ProductSpecification, Company, ProductImages, ProductReview, CheckoutCart
from .form import ReviewForm, ShippingAddress, UserRegisterForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.conf import settings # new
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    mobile_name = request.GET.get('mobile_name', None)
    tab_page = request.GET.get('tab_page', None)

    slider = Product.objects.filter(Slider=True)[:3]
    data = Product.objects.filter(trending=True)[:6]
    mobile_cat = Product.objects.filter(category=1)[:6]
    tab_cat = Product.objects.filter(category=2)[:6]
    spec = ProductSpecification.objects.all()
    mobile = Company.objects.filter(category=1)
    tab_list = Company.objects.filter(category=2)
    if mobile_name is not None:
        mobile_cat = Product.objects.filter(category=1, company=mobile_name)[:6]
    if tab_page is not None:
        tab_cat = Product.objects.filter(category=2, company=tab_page)[:6]

    context = {
        'slider': slider,
        'data': data,
        'mobile_cat': mobile_cat,
        'tab_cat': tab_cat,
        'spec': spec,
        'mobile': mobile,
        'tab_list': tab_list,

    }
    return render(request, 'product/index.html', context)

def product_detail(request, id):
    pro_detail = Product.objects.get(id=id)
    data = request.POST.copy()
    data.update({"product": pro_detail})
    if request.method == 'POST':
        form = ReviewForm(data)
        if form.is_valid():
            form.save()    
    else:
       form = ReviewForm()
    pro_img = ProductImages.objects.filter(product=id)[:6]
    review = ProductReview.objects.filter(product=id)
    context = {
        'pro_detail': pro_detail,
        'pro_img': pro_img,
        'form': form,
        'review': review,        
    }
    return render(request, 'product/product_detail.html', context)
   


@login_required(login_url='/login/')
def checkout_cart(request):
        product_id = request.POST.get('prod_id')
        operation = request.POST.get('operation')
        operation1 = request.POST.get('operation1')
        pro_check = CheckoutCart.objects.filter(product_id=product_id, user=request.user)
        if pro_check.exists():
            cart = CheckoutCart.objects.get(product_id=product_id, user=request.user)
            if operation == 'decrease':
                cart.quantity -= 1
                cart.save()
                if cart.quantity == 0:
                    cart.delete()
            elif operation1 == 'increase':
                cart.quantity += 1
                cart.save()
            else:
                cart.quantity += 1
                cart.save()
        else:
            cart_item = CheckoutCart.objects.create(product_id=product_id, user=request.user)
            cart_item.save()
        
        # product_show = CheckoutCart.objects.all()
        key = settings.STRIPE_PUBLISHABLE_KEY
        product_show = CheckoutCart.objects.filter(user=request.user)
        sub_total = 0
        shipping = 150
        pro_total = 0
        total = 0
        for item in product_show:
            if item.product:
                item.pro_total = item.quantity * item.product.discount_price
                sub_total += item.pro_total 
                total += (sub_total + shipping)
        context = {
            'product_show': product_show,
            'sub_total' : sub_total,
            'total' : total,
            'key' : key,

        }
        return render(request, 'product/checkout_cart.html', context)

@login_required(login_url='/login/')
def checkout_info(request):
    data = request.POST.copy()
    data.update({"user": request.user})
    if request.method == 'POST':
        form = ShippingAddress(data)
        if form.is_valid():
            form.save()
    else:
       form = ShippingAddress()
    context = {
        'form': form,
    }
    return render(request, 'product/checkout_info.html', context)


#signup view
def sign_up(request):
    if request.method =='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'User Can be Registered.')
            form.save()
            return HttpResponseRedirect('/login/')

    else:
        form =UserRegisterForm()
    return render(request, 'product/Authentication/register.html', {'form':form})


# def payment(request):
#     if request.method == 'POST':
#         charge = stripe.Charge.create(
#             amount= 2500,
#             currency='usd',
#             description='Payment Gateway',
#             source=request.POST['stripeToken']
#         )
    
#     return render(request, 'product/checkout_payment.html')

def charge(request):
    if request.method == 'POST':
        total = request.POST.get('total')
        charge = stripe.Charge.create(
            amount=int(float(total)),
            currency='usd',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request, 'product/charge.html')





#login view
def user_login(request):
    # if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Login can be Successfully.')
                    return HttpResponseRedirect('/')
        else:
            form = AuthenticationForm()
        return render(request, 'product/Authentication/login.html', {'form':form})
    # else:
    #     return HttpResponseRedirect('/index/')


#logout
def user_logout(request):

    logout(request)
    return HttpResponseRedirect('/')

#change password with old password
# def user_change_pass(request):
#      if request.user.is_authenticated:
#         if request.method == 'POST':
#                 fm = PasswordChangeForm(user=request.user, data=request.POST)
#                 if fm.is_valid():
#                     fm.save()
#                     update_session_auth_hash(request, fm.user)
#                     messages.success(request, 'password can be changed.')
#                     return HttpResponseRedirect('/profile/')
#         else:     
#          fm = PasswordChangeForm(user=request.user)
#         return render(request, 'myapp/changepass.html', {'form':fm})
#      else:
#         return HttpResponseRedirect('/login/')

# #change password without old password
# def user_change_pass1(request):
#      if request.user.is_authenticated:
#         if request.method == 'POST':
#                 fm =SetPasswordForm(user=request.user, data=request.POST)
#                 if fm.is_valid():
#                     fm.save()
#                     update_session_auth_hash(request, fm.user)
#                     messages.success(request, 'password can be changed.')
#                     return HttpResponseRedirect('/profile/')
#         else:     
#          fm =SetPasswordForm(user=request.user)
#         return render(request, 'myapp/changepass1.html', {'form':fm})
#      else:
#         return HttpResponseRedirect('/login/')





