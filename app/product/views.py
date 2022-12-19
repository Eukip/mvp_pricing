from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from serializers import StrategyToProductSerializer, FileOperationSerializer


class StrategyToProductView(APIView):

    @swagger_auto_schema(request_body=StrategyToProductSerializer)
    def post(self, request, product_id):
        serializer = StrategyToProductSerializer(context={"product_id": product_id}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UploadFile(APIView):

    @swagger_auto_schema(request_body=FileOperationSerializer)
    def post(self, request):
        serializer = FileOperationSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "File saved",
                            "file_out": serializer.validated_data.get("file_out")},
                            status=status.HTTP_201_CREATED)


