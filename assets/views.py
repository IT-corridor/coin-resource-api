from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import AssetModelSerializer
from .models import Asset


class AssetModelViewSet(ModelViewSet):
    model = Asset
    serializer_class = AssetModelSerializer
    queryset = Asset.objects.all()
    permission_classes = [IsAdminUser]



