# Generated by Django 2.2.4 on 2022-10-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_plan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='Planted_By',
        ),
        migrations.AddField(
            model_name='plan',
            name='location',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
