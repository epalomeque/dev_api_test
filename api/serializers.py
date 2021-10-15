from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    order_number = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=200)

