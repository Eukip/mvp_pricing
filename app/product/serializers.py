from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Product, StrategyProduct, FileModel
from .utils import parse_excel, populate_excel, populate_products_db
from app.strategy.models import Strategy


class StrategyToProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)

    def validate(self, attrs):
        strategy = get_object_or_404(Strategy, pk=attrs["id"])
        product_number = self.context.get('product_id')
        product = get_object_or_404(Product, pk=product_number)
        if StrategyProduct.objects.filter(product_id=product_number, strategy_id=attrs("id")).exists():
            return Response("Strategy already assigned to the product", status=status.HTTP_409_CONFLICT)
        return attrs

    def create(self, validated_data):
        product_number = self.context.get('product_id')
        return StrategyProduct.objects.create(product_id=product_number, strategy_id=validated_data.get("id"))


class FileOperationSerializer(serializers.Serializer):

    file_in = serializers.FileField(allow_empty_file=False)

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        title = str(validated_data.get("file_in"))
        content = parse_excel(title)
        file_out = populate_excel(title)
        return FileModel.objects.create(title=title,
                                        file_in=validated_data.get("file_in"),
                                        file_out=file_out,
                                        content=content)


