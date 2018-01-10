from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import AssetModelSerializer, SoldAssetModelSerializer
from .models import Asset, SoldAssets


class AssetModelViewSet(ModelViewSet):
    model = Asset
    serializer_class = AssetModelSerializer
    queryset = Asset.objects.all()
    permission_classes = [IsAdminUser]


class SoldAssetsModelViewSet(ModelViewSet):
    model = SoldAssets
    queryset = SoldAssets.objects.all()
    serializer_class = SoldAssetModelSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        asset = Asset.objects.get(pk=request.data['id'])
        if request.data['amount'] > asset.amount:
            return Response({'error': 'Check Amount '}, status=status.HTTP_400_BAD_REQUEST)

        else:
            asset.amount -= request.data['amount']
            asset.asset_id = asset.id
            asset.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request['investment_start_date']:
            instance.investment_start_date = request['investment_start_date']
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
