from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=250)
    body = serializers.CharField()
    slug = serializers.CharField()

    class Meta:
        model = Content
        fields = ("__all__")