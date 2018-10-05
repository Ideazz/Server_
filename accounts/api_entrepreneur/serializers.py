from rest_framework import serializers
from ..models import Entrepreneur

class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
          model=Entrepreneur
          fields=('id','username','refral_created','refral_accessed','city','state','country','description','current_occupation','date_of_birth','Is_investor')
