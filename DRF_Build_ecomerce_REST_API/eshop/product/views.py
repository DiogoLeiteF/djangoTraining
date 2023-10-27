from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import Productsfilter
from .models import Product, ProductImages
from .serializers import ProductSerializer, ProductImagesSerializer


# Create your views here.

@api_view(['GET'])
def get_products(request):
    filterset = Productsfilter(request.GET, queryset=Product.objects.all().order_by("id"))

    count = filterset.qs.count()

    # Pagination
    resPerPage = 2
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ProductSerializer(queryset, many=True)
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    return Response({
        "count": count,
        "resPerPage": resPerPage,
        "products": serializer.data
    })


@api_view(["GET"])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({"product": serializer.data})


@api_view(["POST"])
def new_product(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"Error": "invalid method"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def upload_product_images(request):
    data = request.data
    files = request.FILES.getlist("images")

    images = []
    for f in files:
        print("F", f)
        image = ProductImages.objects.create(product=Product(data["product"]), image=f)
        images.append(image)

    serializer = ProductImagesSerializer(images, many=True)

    return Response(serializer.data)


@api_view(["PUT"])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    # TODO check if user is same

    # cannot use because of serializer validator
    # if request.method == "PUT":
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response({"error": "invalid method"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        if request.data.get("name"):
            product.name = request.data.get("name")
        if request.data.get("description"):
            product.description = request.data.get("description")
        if request.data.get("price"):
            product.price = request.data.get("price")
        if request.data.get("brand"):
            product.brand = request.data.get("brand")
        if request.data.get("ratings"):
            product.ratings = request.data.get("ratings")
        if request.data.get("category"):
            product.category = request.data.get("category")
        if request.data.get("stock"):
            product.stock = request.data.get("stock")

        product.save()

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"error": "invalid method"}, status=status.HTTP_400_BAD_REQUEST)
