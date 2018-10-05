from rest_framework import serializers
from ..models import Ideator

class IdeatorSerializers(serializers.ModelSerializer):
    class Meta:
             model=Ideator
             fields=('id','username','city','state','country','description','current_occupation','date_of_birth')
