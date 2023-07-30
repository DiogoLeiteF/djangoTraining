import json

from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.


# def api_home(request, *args, **kwargs) -> JsonResponse:
#     body = request.body # byte string of json date
#     print(request.GET) #access the params form request "/?key=value"
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     data["params"] = dict(request.GET)
#     print(data)
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()

#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         data = model_to_dict(model_data, fields=["id", "price"])
#     return JsonResponse(data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=["id", "title", "price"])
#         data= ProductSerializer(instance).data
#     return Response(data)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    
