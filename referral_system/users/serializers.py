from rest_framework import serializers
from .models import User, Referral

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'referral_code', 'date_joined']

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ['referring_user', 'referred_user', 'timestamp']
