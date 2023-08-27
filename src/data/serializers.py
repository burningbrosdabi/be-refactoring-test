from rest_framework import serializers
from .models import Campaign, AdSet, Creative, Account


class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = '__all__'

class AdSetSerializer(serializers.ModelSerializer):
    creatives = CreativeSerializer(many=True)

    class Meta:
        model = AdSet
        fields = '__all__'
        
class CampaignSerializer(serializers.ModelSerializer):
    adsets = AdSetSerializer(many=True)

    class Meta:
        model = Campaign
        fields = (
                    "id",
                    "campaign_name",
                    "campaignNo",
                    "cost",
                    "targetDate",
                    "clickCount",
                    "convCount",
                    "convSales",
                    "user",
                    "account",
                    "adsets"
        )

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
