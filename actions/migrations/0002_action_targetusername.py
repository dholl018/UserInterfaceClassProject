# Generated by Django 3.2.8 on 2021-11-20 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='targetUsername',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
