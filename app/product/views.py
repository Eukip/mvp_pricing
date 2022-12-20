from .serializers import FileOperationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .wb_search import get_wb_catalog_filter_by_query, get_seller_by_product_article, get_product_by_article


class SearchProductWB(APIView):

    def get(self, request):
        product_id = self.request.query_params.get("product_id")
        search_query = self.request.query_params.get("search_query")
        seller_by_article = self.request.query_params.get("seller_by_article")

        if product_id:
            product_by_article = get_product_by_article(product_id)
            return Response(status=status.HTTP_200_OK, data=product_by_article)
        
        if search_query:
            search_result = get_wb_catalog_filter_by_query(search_query)
            return Response(status=status.HTTP_200_OK, data=search_result)

        if seller_by_article:
            seller = get_seller_by_product_article(int(seller_by_article))
            return Response(status=status.HTTP_200_OK, data=seller)

        return Response(status=status.HTTP_400_BAD_REQUEST)