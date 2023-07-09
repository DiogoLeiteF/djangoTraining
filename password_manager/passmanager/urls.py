"""
URL configuration for password_manager project.

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

from django.urls import path
from passmanager import views

urlpatterns = [
    
    path('', views.index, name="Home"),
    path('manager/', views.manager, name="manager"),
    path('signup/', views.sign_up, name="signup"),
    path('log-out/', views.log_out, name="logout"),
    path('edit/', views.edit_data, name="edit"),
    path('new/', views.new_data, name="new"),
    path('delete/', views.delete_data, name="delete"),
    
]
