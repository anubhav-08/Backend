# Generated by Django 3.1.4 on 2020-12-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0011_auto_20201216_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='index',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
