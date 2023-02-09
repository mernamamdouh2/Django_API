from django.db.models import fields
from rest_framework import serializers
from .models import Publisher

class publisherserializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields=('name','email')