from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import StrategyProduct
from product.serializers import StrategyToProductSerializer


class StrategyListCreateView(APIView):
    serializer_class = StrategyToProductSerializer

    def get(self, request, *args, **kwargs):
        product_id = self.request.query_params.get("product_id")
        queryset = StrategyProduct.objects.filter(product__id=product_id)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        product_id = self.request.query_params.get("product_id")
        serializer = self.serializer_class(context={"product_id": product_id}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
