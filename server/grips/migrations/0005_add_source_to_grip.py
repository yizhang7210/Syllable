# Generated by Django 2.1.4 on 2019-01-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grips', '0004_add_user_grip_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='grip',
            name='source',
            field=models.TextField(blank=True),
        ),
    ]
