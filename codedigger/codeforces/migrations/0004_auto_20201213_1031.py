# Generated by Django 3.1.4 on 2020-12-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeforces', '0003_auto_20201213_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
