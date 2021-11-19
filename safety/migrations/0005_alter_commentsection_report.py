# Generated by Django 3.2.8 on 2021-11-04 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0004_commentsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsection',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='safety.safetyreport'),
        ),
    ]
