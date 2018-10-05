from rest_framework import generics
from ..models import Ideator
from .serializers import IdeatorSerializers

class IdeatorPutViews(generics.RetrieveUpdateDestroyAPIView):
    lookup_field= 'pk'
    serializer_class = IdeatorSerializers

    def get_queryset(self):
        return Ideator.objects.all()

class IdeatorCreateViews(generics.ListAPIView):
    lookup_field= 'pk'
    serializer_class= IdeatorSerializers

    def get_queryset(self):
        return Ideator.objects.all()

    def preform_create(self,serializer):
         serializer.save(user=self.request.user)
