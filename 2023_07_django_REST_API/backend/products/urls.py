from django.urls import path


from . import views


urlpatterns = [
    # path("<int:pk>/", view=views.ProductDetailAPIView.as_view()),
    # path("", view=views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/", view=views.product_alt_view),
    path("", view=views.product_alt_view),
]
