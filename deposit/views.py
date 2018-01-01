from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import DepositModelSerializer, UserDepositModelSerializer, PublicUserDepositModelSerializer
from .models import Deposit
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response


class DepositModelViewSet(ModelViewSet):
    model = Deposit
    queryset = Deposit.objects.all()
    serializer_class = DepositModelSerializer
    permission_classes = [IsAdminUser]

    @list_route(methods=['GET'])
    def get_user_deposits(self, request):
        user_deposits = Deposit.objects.filter(owner=request.pk)
        print(user_deposits)
        serializer = self.get_serializer(user_deposits, many=True)
        return Response(serializer.data)


class UserDepositModelViewSet(ModelViewSet):
    model = Deposit
    serializer_class = UserDepositModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deposit.objects.filter(owner=self.request.user)


class PublicUserDepositModelViewSet(ModelViewSet):
    model = Deposit
    queryset = Deposit.objects.all()
    serializer_class = PublicUserDepositModelSerializer
    permission_classes = [IsAuthenticated]

