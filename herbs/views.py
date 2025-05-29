
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Herb
from django.db.models import Q



def home(request):
    return render(request, 'herbs/home.html')

def herb_list(request):
    query = request.GET.get('q')
    herbs = Herb.objects.all()

    if query:
        herbs = herbs.filter(
            Q(local_name__icontains=query) |
            Q(english_name__icontains=query) |
            Q(scientific_name__icontains=query) |
            Q(common_use__icontains=query) |
            Q(location__icontains=query)
            
  
        )

    return render(request, 'herbs/herb_list.html', {'herbs': herbs})


def herb_detail(request, pk):  # Accept pk here
    herb = get_object_or_404(Herb, pk=pk)
    return render(request, 'herbs/herb_detail.html', {'herb': herb})

from rest_framework import generics
from .models import Herb
from .serializers import HerbSerializer

class HerbListAPI(generics.ListAPIView):
    queryset = Herb.objects.all()
    serializer_class = HerbSerializer

class HerbDetailAPI(generics.RetrieveAPIView):
    queryset = Herb.objects.all()
    serializer_class = HerbSerializer





