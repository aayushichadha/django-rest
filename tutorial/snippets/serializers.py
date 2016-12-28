from rest_framework import serializers
from snippets.models import Number


class NumberSerializer(serializers.Serializer):
    class Meta:
        model = Number
        fields = 'Value'
