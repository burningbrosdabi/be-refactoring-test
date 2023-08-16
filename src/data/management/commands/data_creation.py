import random
from faker import Faker
from data.models import Account, Campaign, AdSet, Creative, CustomUser
from django.core.management.base import BaseCommand


# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = "refresh"

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"
MODE_PROD = "prod"

fake = Faker()

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        generate_test_data()
        self.stdout.write("done.")


def generate_test_data():
    # Create 4 accounts
    accounts = []
    for _ in range(4):
        account = Account.objects.create(
            name=fake.company(),
            adAccountNo=fake.unique.random_number(digits=5),
            user=CustomUser.objects.first()
        )
        accounts.append(account)

    # Create 26 campaigns
    campaigns = []
    for _ in range(26):
        campaign = Campaign.objects.create(
            user=CustomUser.objects.first(),
            account=random.choice(accounts),
            campaign_name=fake.sentence(),
            campaignNo=fake.unique.random_number(digits=6),
            cost=random.uniform(100, 10000),
            targetDate=fake.date(),
            clickCount=random.randint(100, 1000),
            convCount=random.uniform(10, 100),
            convSales=random.uniform(1000, 10000)
        )
        campaigns.append(campaign)

    # Create 300 adsets
    adsets = []
    for _ in range(300):
        adset = AdSet.objects.create(
            user=CustomUser.objects.first(),
            campaign=random.choice(campaigns),
            account=random.choice(accounts),
            adset_name=fake.sentence(),
            adSetNo=fake.unique.random_number(digits=6),
            cost=random.uniform(100, 10000),
            targetDate=fake.date(),
            clickCount=random.randint(100, 1000),
            convCount=random.uniform(10, 100),
            convSales=random.uniform(1000, 10000)
        )
        adsets.append(adset)

    # Create 996 creatives
    for _ in range(996):
        Creative.objects.create(
            user=CustomUser.objects.first(),
            ad_set=random.choice(adsets),
            account=random.choice(accounts),
            creative_name=fake.sentence(),
            creativeNo=fake.unique.random_number(digits=6),
            creativeType=random.choice(['Type 1', 'Type 2', 'Type 3']),
            cost=random.uniform(100, 10000),
            targetDate=fake.date(),
            clickCount=random.randint(100, 1000),
            convCount=random.uniform(10, 100),
            convSales=random.uniform(1000, 10000)
        )
