# Generated by Django 3.2.18 on 2023-04-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]