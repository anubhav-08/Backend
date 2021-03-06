# Generated by Django 3.1.4 on 2020-12-17 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeforces', '0007_auto_20201213_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='number',
            new_name='current',
        ),
        migrations.RenameField(
            model_name='country_contest_participation',
            old_name='number',
            new_name='current',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='number',
            new_name='current',
        ),
        migrations.RenameField(
            model_name='organization_contest_participation',
            old_name='number',
            new_name='current',
        ),
        migrations.AddField(
            model_name='country',
            name='total',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country_contest_participation',
            name='total',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='total',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization_contest_participation',
            name='total',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]
