# Generated by Django 2.1.4 on 2019-01-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_add_domain_to_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='domain',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
