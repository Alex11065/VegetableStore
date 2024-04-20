from django.urls import path
from .views import IndexShopView, AboutSopView, ContactSopView

app_name = "home"

urlpatterns = [
    path('', IndexShopView.as_view(), name="index"),
    path('about/', AboutSopView.as_view(), name="about"),
    path('contact/', ContactSopView.as_view(), name="contact"),
]
