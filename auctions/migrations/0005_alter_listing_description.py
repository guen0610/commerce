# Generated by Django 4.1 on 2022-08-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]