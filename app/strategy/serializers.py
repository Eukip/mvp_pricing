from rest_framework import serializers

from .models import Strategy

class StrategyCreateSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=300)
    priority = serializers.IntegerField(required=False, default=0)
    is_active = serializers.BooleanField(default=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    logic = serializers.JSONField(required=False, allow_blank=True, allow_null=True)
    journals = serializers.JSONField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Strategy.objects.create(title=validated_data.get('title'),
                                       priority=validated_data.get('priority'),
                                       is_active=validated_data.get('is_active'),
                                       description=validated_data.get('description'),
                                       logic=validated_data.get('logic'),
                                       journals=validated_data.get('journals'))