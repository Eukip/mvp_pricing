from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from def_yasg.utils import swagger_auto_schema

from .models import Strategy
from .serializers import StrategyCreateSerializer


class StrategyCreateView(APIView):

    def get(self, request):
        queryset = Strategy.objects.all()
        serializer = StrategyCreateSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=StrategyCreateSerializer)
    def post(self, request):
        serializer = StrategyCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

