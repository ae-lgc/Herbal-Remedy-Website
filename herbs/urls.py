from . import views
from django.shortcuts import render, get_object_or_404
from .models import Herb
from django.urls import path
from .views import HerbListAPI, HerbDetailAPI


urlpatterns = [
    path('', views.herb_list, name='list'),
    path('herb/', views.herb_list, name='herb_list'),
    path('', views.home, name='home'), 
    path('herb/<int:pk>/', views.herb_detail, name='herb_detail'),
    path('api/herbs/', HerbListAPI.as_view(), name='api-herb-list'),
    path('api/herbs/<int:pk>/', HerbDetailAPI.as_view(), name='api-herb-detail'),
 
]

def herb_list(request):
    herbs = Herb.objects.all()
    return render(request, 'herbs/herb_list.html', {'herbs': herbs})

def herb_detail(request, id):
    herb = get_object_or_404(Herb, id=id)
    return render(request, 'herbs/herb_detail.html', {'herb': herb})

