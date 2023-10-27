from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.get_products, name="products"),
    path("products/upload_images/", views.upload_product_images, name="upload_product_images"),
    path("products/new/", views.new_product, name="new_product"),
    path("products/<str:pk>/", views.get_product, name="get_product_details"),
]

