from rest_framework import serializers
from ..models import Ideas

class IdeaSerializer(serializers.ModelSerializer):
       class Meta:
            model=Ideas
            fields=('id','username','ideator','Is_patent','subject')

       def create(self, validated_data):
            return Ideas.objects.create(**validated_data)

       def update(self, instance, validated_data):
             instance.username = validated_data.get('username', instance.username)
             instance.subject = validated_data.get('subject', instance.subject)
             instance.save()
             return instance

class IdeaSerializerDetails(serializers.ModelSerializer):
       class Meta:
            model=Ideas
            fields=('id','username','ideator','Is_patent','subject','description','expectation')

       def create(self, validated_data):
            return Ideas.objects.create(**validated_data)

       def update(self, instance, validated_data):
             instance.username = validated_data.get('username', instance.username)
             instance.subject = validated_data.get('subject', instance.subject)
             instance.save()
             return instance
