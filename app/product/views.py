
from serializers import FileOperationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UploadFile(APIView):

    def post(self, request):
        serializer = FileOperationSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "File saved",
                            "file_out": serializer.validated_data.get("file_out")},
                            status=status.HTTP_201_CREATED)

