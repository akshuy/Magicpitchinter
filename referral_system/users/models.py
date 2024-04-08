from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    referral_code = models.CharField(max_length=20, blank=True, null=True)

class Referral(models.Model):
    referring_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred_by')
    timestamp = models.DateTimeField(auto_now_add=True)
