# Generated by Django 3.1.4 on 2020-12-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeforces', '0005_auto_20201213_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_contest_rank',
            name='countryRank',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='user_contest_rank',
            name='organisationRank',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
