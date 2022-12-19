from rest_framework import serializers
from .utils import parse_excel, populate_excel, populate_products_db
from .models import Product, StrategyProduct, FileModel
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
