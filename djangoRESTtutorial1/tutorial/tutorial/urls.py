"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
# router.register(r"users", views.UserViewSet)
# router.register(r"groups", views.GroupViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    
    # path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("movies/", views.movies_list, name="movies"),
    # path("movie/<int:pk>", views.movie_detail, name="movie details"),
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>", views.SnippetDetail.as_view()),

]

# does not work with routers
urlpatterns = format_suffix_patterns(urlpatterns)
