from django.urls import path
from . import views

app_name = "brands"

urlpatterns = [
    path('<slug:slug>/', views.product_list, name='product_list'),
]
