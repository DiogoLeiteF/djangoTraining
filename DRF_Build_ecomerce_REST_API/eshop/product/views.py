from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import Productsfilter
from .models import Product, ProductImages, Review
from .serializers import ProductSerializer, ProductImagesSerializer, ReviewSerializer


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
@permission_classes([IsAuthenticated])
def new_product(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data, user=request.user)
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
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if not product.user == request.user:
        return Response({"error": "You cannot update this product"}, status=status.HTTP_401_UNAUTHORIZED)

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


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if not product.user == request.user:
        return Response({"error": "You cannot delete this product"}, status=status.HTTP_401_UNAUTHORIZED)

    # delete from ProductImages
    args = {"product": pk}
    images = ProductImages.objects.filter(**args)
    for i in images:
        i.delete()

    # delete product
    product.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_review(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    data = request.data
    print(data)

    review = Review.objects.filter(user=user, product=product)

    if not data.get("rating"):
        return Response({"error": "Rating is required"}, status=status.HTTP_400_BAD_REQUEST)

    if data["rating"] <= 0 or data["rating"] > 5:
        return Response({"error": "Rating must be between 1-5"}, status=status.HTTP_400_BAD_REQUEST)

    if review.exists():
        new_review = {"rating": data["rating"], "comment": data.get("comment")}
        review.update(**new_review)

        # calculate the avg of ratings with aggregate
        update_product_rating(product=product)

        return Response({"detail": "review updated"}, status=status.HTTP_200_OK)

    new_review = {
        "rating": data["rating"],
        "comment": data.get("comment"),
        "user": user.id,
        "product": product.id
    }
    serializer = ReviewSerializer(data=new_review, many=False)
    if serializer.is_valid():
        serializer.save()

        # calculate the avg of ratings with aggregate
        update_product_rating(product=product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_reviews(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ReviewSerializer(product.reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    review = get_object_or_404(Review, product=pk, user=user.id)
    review.delete()

    # calculate the avg of ratings with aggregate
    update_product_rating(product=product)

    return Response({"detail": "review deleted"}, status=status.HTTP_200_OK)


def update_product_rating(product: Product):
    # calculate the avg of ratings with aggregate
    ratings = product.reviews.aggregate(avg_ratings=Avg("rating"))
    ratings["avg_ratings"] = ratings["avg_ratings"] or 0
    product.ratings = ratings["avg_ratings"]
    product.save()
