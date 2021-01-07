# Generated by Django 1.11.15 on 2018-08-21 16:36


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_auto_20180817_1929"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("records", "0014_auto_20180820_2032"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercreditpathway",
            name="credit_pathway",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="catalog.CreditPathway"),
        ),
        migrations.AlterUniqueTogether(
            name="usercreditpathway",
            unique_together={("user", "pathway")},
        ),
    ]
