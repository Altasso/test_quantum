"""
URL configuration for blog_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog_api/', include('blog_api.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from blog.api import router as blog_router

api = NinjaAPI()

api.add_router("/blog/", blog_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
