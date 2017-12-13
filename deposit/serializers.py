from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Deposit
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.registration.views import RegisterView

User = get_user_model()


class DepositModelSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            'id',
            'owner',
            'amount',
            'created',   
        ]
        read_only_fields = ('id',)

class UserDepositModelSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            'id',
            'owner',
            'amount',
            'created',   
        ]
        read_only_fields = ('id',)

