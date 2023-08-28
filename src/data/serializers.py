from rest_framework import serializers
from .models import Campaign, AdSet, Creative, Account, User
from django.contrib.auth import authenticate, login


class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = "__all__"


class AdSetSerializer(serializers.ModelSerializer):
    creatives = CreativeSerializer(many=True)

    class Meta:
        model = AdSet
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    adsets = AdSetSerializer(many=True)

    class Meta:
        model = Campaign
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class UserLoginSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        password = attrs.get("password")

        if not user_id or not password:
            raise serializers.ValidationError("Must include 'user_id' and 'password'.")
        try:
            username = User.objects.get(pk=user_id).username
        except User.DoesNotExist as e:
            raise serializers.ValidationError("User does not exist.") from e

        if not (user := authenticate(username=username, password=password)):
            raise serializers.ValidationError(
                "Unable to log in with provided credentials."
            )
        if not user.is_active:
            raise serializers.ValidationError("This user account is inactive.")

        attrs["user"] = user
        return attrs
