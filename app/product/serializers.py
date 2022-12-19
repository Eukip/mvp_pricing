from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Product, StrategyProduct
from strategy.models import Strategy
from strategy.serializers import StrategySerializer

class StrategyToProductSerializer(serializers.ModelSerializer):
    strategy = StrategySerializer()

    class Meta:
        model = StrategyProduct
        fields = ['strategy']
    
    def create(self, validated_data):
        strategy_data = validated_data.pop('strategy')
        product = Product.objects.get(id=self.context.get("product_id"))
        sp = StrategyProduct.objects.create(
            product=product, **strategy_data
        )
        return sp.strategy
