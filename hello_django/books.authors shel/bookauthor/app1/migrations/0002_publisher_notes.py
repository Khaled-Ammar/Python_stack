# Generated by Django 2.2.4 on 2022-09-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
