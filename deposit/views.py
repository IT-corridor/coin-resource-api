from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import DepositModelSerializer, UserDepositModelSerializer
from .models import Deposit

class DepositModelViewSet(ModelViewSet):
    model =  Deposit
    queryset = Deposit.objects.all()
    serializer_class = DepositModelSerializer
    permission_classes = [IsAdminUser]

class UserDepositModelViewSet(ModelViewSet):
    model = Deposit
    serializer_class = DepositModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Deposit.objects.filter(owner=self.request.user)