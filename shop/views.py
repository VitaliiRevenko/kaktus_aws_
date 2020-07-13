from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Create your views here.



def main_page(request):
    return render(request,'index.html', {
        "catlist": Category.objects.filter(parent_category=None),
        "productlist": Product.objects.order_by('-pk')[:20]

    })

def config_context(request):
    return {'PRIMARY_PHONE': '0682707080', 'SECOND_PHONE': '0682700770', 'CONTACT_EMAIL': 'info@vrevenko.com',
            'FACEBOOK': 'www.facebook.com/vitaliy.revenko', 'INSTAGRAM': 'www.instagram.com/vrevenko',
            'PINTEREST': 'www.pinterest.com/vitaliyrevenko', 'EMAIL': 'vitalirevenko84@gmail.com'}

def delivery_and_pay(request):
    return render(request, 'delivery_pay.html')

def info_about_us(request):
    return render(request, 'about_us.html')

def contact_me(request):
    return render(request, 'contact.html')

def category_view(request, **kwargs):

    return render(request, 'category.html', {
        "cat": get_object_or_404(Category, pk=kwargs.get('id_category')),
    })

def product_detail(request, pk):
    return render(request, 'full_product.html', {
        "item": get_object_or_404(Product, pk=pk)
    })

class CategoryView(APIView):
    def get(self, request):
        name = Category.objects.all()
        return Response({"name": name})