from rest_framework import serializers
from test_app.models import UnionBoard

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionBoard
        fields = '__all__'
