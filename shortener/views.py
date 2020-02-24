from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class ShortenerView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        links = models.Link.objects.all()
        serializer = serializers.LinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
