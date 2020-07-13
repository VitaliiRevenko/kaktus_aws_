"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from shop import views
from shop.views import main_page, category_view, product_detail, contact_me
from shop.views import CategoryView

from rest_framework import routers

##########

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

##########



app_name = "shop"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='index'),

    path('shop/', CategoryView.as_view()),
    #path('api/', include('site.urls')),
    path('category/<int:id_category>/', category_view, name='one_category'),
    path('product/<int:pk>/', product_detail, name='one_product'),
    ##
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ##
    path('contact', contact_me, name='contact' )
]
