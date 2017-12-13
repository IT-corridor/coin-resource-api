from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import DepositModelSerializer, UserDepositModelSerializer
from .models import Deposit

class DepositModelViewSet(ModelViewSet):
    model =  Deposit
    queryset = Deposit.objects.all()
    serializer_class = DepositModelSerializer

class UserDepositModelViewSet(ModelViewSet):
    model = Deposit
    serializer_class = DepositModelSerializer

    def get_queryset(self, request):
        return Deposit.objects.filter(owner=request.user)