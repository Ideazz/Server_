from rest_framework import generics
from ..models import Entrepreneur
from .serializers import EntrepreneurSerializer

class EntrepreneurPutView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field =  'pk'
    serializer_class = EntrepreneurSerializer

    def get_queryset(self):
         return Entrepreneur.objects.all()


class EntrepreneurCreateView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EntrepreneurSerializer

    def get_queryset(self):
         return Entrepreneur.objects.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
