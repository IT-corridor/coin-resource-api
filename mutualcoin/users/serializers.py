from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.registration.views import RegisterView

User = get_user_model()


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'zip_code',
            'pin',
            'approved',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'phone',
            'first_name',
            'last_name',
            'date_joined', 
            'last_login'            
        ]

        read_only_fields = (
            'id',
        )

        def update(self, instance, validated_data):
            instance.phone = validated_data.get('phone', instance.phone)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.save()
            return instance
        #
        # def get_user_sell_orders(request):
        #     return SellOrder.objects.filter(user=request.data['user'])


class AdminUserSerializer(ModelSerializer):
    class Meta:
        model = User
        phone = serializers.CharField(required=False)
        fields = [
            'id',
            'zip_code',
            'pin',
            'approved',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'phone',
            'first_name',
            'last_name',
            'date_joined', 
            'last_login'            
        ]
        read_only_fields = ('email','phone' 'zip_code', 'pin' )

    def update(self, instance, validated_data):
        print(instance)
        if instance.approved :
            instance.approved = False
        else:
            instance.approved = True
        instance.save()
        return instance

class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()



    


