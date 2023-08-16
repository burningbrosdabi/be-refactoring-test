from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from data.models import Campaign, AdSet, Creative, Account, CustomUser

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('adAccountNo', 'name', 'user', )

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'account',
                    'campaign_name', 
                    'campaignNo', 
                    'cost',
                    
                    'clickCount',
                    'convSales',
                    'convCount',
                    )

@admin.register(AdSet)
class AdSetAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'account',
                    'campaign',
                    'adset_name', 
                    'adSetNo', 
                    'cost',
                    
                    'clickCount',
                    'convSales',
                    'convCount',
                    )
    
@admin.register(Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'account',
                    'ad_set',
                    'creative_name', 
                    'creativeNo', 
                    'cost',
                    
                    'clickCount',
                    'convSales',
                    'convCount',
                    )