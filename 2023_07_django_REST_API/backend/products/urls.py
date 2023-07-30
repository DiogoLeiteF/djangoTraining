from django.urls import path


from . import views


urlpatterns = [
    path("<int:pk>/", view=views.ProductDetailAPIView.as_view()),
    path("", view=views.ProductListCreateAPIView.as_view()),
]
