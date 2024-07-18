"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path

from person.views import Createfood, listfood, Updatefood, deletefood, createcategory, listcategory, Updatecategory, \
    deletecategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/createfood/', Createfood.as_view()),
    path('api/v1/listfood/', listfood.as_view()),
    path('api/v1/updatefood/<int:pk>/', Updatefood.as_view()),
    path('api/v1/deletefood/<int:pk>/', deletefood.as_view()),
    path('api/v1/createcategory/', createcategory.as_view()),
    path('api/v1/listcategory/', listcategory.as_view()),
    path('api/v1/updatecategory/<int:pk>/', Updatecategory.as_view()),
    path('api/v1/deletecategory/<int:pk>/', deletecategory.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
