
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from ..data_creation import generate_test_data

def test_data_generator(apps, schema_editor):
    generate_test_data()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=test_data_generator,
        )
    ]
