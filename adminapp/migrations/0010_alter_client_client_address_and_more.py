# Generated by Django 4.0.4 on 2022-04-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_client_client_id_client_client_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_address',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_contact_type',
            field=models.CharField(default='', max_length=40),
        ),
    ]
