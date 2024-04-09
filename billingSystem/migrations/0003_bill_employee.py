# Generated by Django 4.2.11 on 2024-04-09 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billingSystem', '0002_bill_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_bills', to=settings.AUTH_USER_MODEL),
        ),
    ]