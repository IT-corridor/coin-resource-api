from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Asset, SoldAssets
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.registration.views import RegisterView

User = get_user_model()


class AssetModelSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'id',
            'name',
            'symbol',
            'image_url',
            'buy_price',
            'sell_price',
            'currency',
            'price_type',
            'purchase_price',
            'transaction_date',
            'amount',
            'note',
            'created',
            'modified'
        ]
        read_only_fields = ('id',)


class SoldAssetModelSerializer(ModelSerializer):
    class Meta:
        model = SoldAssets
        fields = [
            'id',
            'name',
            'symbol',
            'image_url',
            'asset_id',
            'sell_price',
            'currency',
            'price_type',
            'transaction_date',
            'market_price',
            'amount',
            'note',
            'created',
            'modified'
        ]
        read_only_fields = ('id',)
