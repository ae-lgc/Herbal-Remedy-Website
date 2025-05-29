from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Herb
from .serializers import HerbSerializer  # siguroa nga naa pud ka ani

class HerbListAPI(APIView):
    def get(self, request):
        herbs = Herb.objects.all()
        serializer = HerbSerializer(herbs, many=True)
        return Response(serializer.data)
