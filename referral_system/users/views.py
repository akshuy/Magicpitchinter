from rest_framework import status
from rest_framework.response import Response
from .models import User, Referral
from .serializers import UserSerializer, ReferralSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        # Check if there's a referral code provided
        referral_code = data.get('referral_code')
        if referral_code:
            referred_by = User.objects.filter(referral_code=referral_code).first()
            if referred_by:
                Referral.objects.create(referring_user=referred_by, referred_user=user)
        return Response({'user_id': user.id, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def user_referrals(request):
    user = request.user
    referrals = Referral.objects.filter(referring_user=user)
    serializer = ReferralSerializer(referrals, many=True)
    return Response(serializer.data)
