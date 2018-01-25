# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import random

from allauth import app_settings
from allauth.account.views import ConfirmEmailView
from django.http import Http404
from django.http import JsonResponse
from django.views import View
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .models import User, UserLoginHistory
from .serializers import UserModelSerializer, AdminUserSerializer, VerifyEmailSerializer, UserLoginHistorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.decorators import list_route, detail_route
from datetime import datetime, timedelta
from pytrends.request import TrendReq

PERIODS = {
    24: 'now 1-d',
    150: 'now 7-d',
    720: 'today 1-m',
    2000: 'today 3-m'
}

@api_view()
def null_view(request):
    pass
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def getTrends(request, keyword, period):
    pytrend = TrendReq()
    period = int(period)

    if period in PERIODS:
        timeframe = PERIODS[period]
    else:
        end = datetime.now().strftime('%Y-%m-%d')
        start = (datetime.now() - timedelta(days=period)).strftime('%Y-%m-%d')
        timeframe = '{} {}'.format(start, end)

    pytrend.build_payload([keyword], timeframe=timeframe)
    interest_over_time_df = pytrend.interest_over_time()

    result = []
    for index, row in interest_over_time_df.iterrows():
        result.append({
            'date': str(index),
            'value': row[keyword], 
            'volumne': random.randint(1, 22)
        })

    return JsonResponse(result, safe=False)


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)

confirm_email = VerifyEmailView.as_view()


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()


class UserModelViewSet(LoggingMixin, ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # permission_classes = [IsAuthenticated]

    @list_route(methods=['post', 'put'])
    def approve_user(self, request):
        print(request['id'])
        return None

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AdminUserModelViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginHistoryModelViewSet(ModelViewSet):
    model = UserLoginHistory
    serializer_class =  UserLoginHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserLoginHistory.objects.filter(user=self.request.user)


class GetUserLoginHistoryModelViewSet(ModelViewSet):
    model = UserLoginHistory
    queryset = UserLoginHistory.objects.all()
    serializer_class = UserLoginHistorySerializer
    permission_classes = [IsAdminUser]


