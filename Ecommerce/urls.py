from django.contrib import admin
from django.urls import path, include
from product import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('detail/<int:id>/', views.product_detail, name="detail"),
    path('checkout_cart/', views.checkout_cart, name="checkout_cart"),
    path('checkout_info/', views.checkout_info, name="checkout_info"),
    path('charge/', views.charge, name="charge"),
    # path("stripe/", include("djstripe.urls", namespace="djstripe")),
    # path('search/', views.search_result),
    # path('index2/', views.index2),
    # path('myaccount/', views.my_account),
    # path('product/', views.product),

    # Auth
    path('register/', views.sign_up, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    # path("stripe/", include("djstripe.urls", namespace="djstripe")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
