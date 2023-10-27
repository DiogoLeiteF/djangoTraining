from django_filters import rest_framework as filters
from .models import Product


class Productsfilter(filters.FilterSet):

    # to look for a specific keyword in some field
    keyword = filters.CharFilter(field_name="name", lookup_expr="icontains")
    min_price = filters.NumberFilter(field_name="price" or 0, lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price" or 1000000, lookup_expr="lte")

    class Meta:
        model = Product
        fields = ("max_price", "min_price", "keyword", "category", "brand")


