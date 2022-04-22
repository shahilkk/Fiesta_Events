# Generated by Django 4.0.4 on 2022-04-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_holdername', models.CharField(max_length=50)),
                ('bank_ifsc', models.CharField(max_length=30)),
                ('bank_accountname', models.CharField(max_length=30)),
                ('bank_balance', models.IntegerField()),
            ],
            options={
                'db_table': 'AddBank',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_gst_number', models.CharField(max_length=30)),
                ('client_id', models.CharField(max_length=30)),
                ('client_phone', models.CharField(max_length=30)),
                ('client_email', models.CharField(max_length=30)),
                ('client_state', models.CharField(max_length=30)),
                ('client_district', models.CharField(max_length=30)),
                ('client_zipcode', models.CharField(max_length=30)),
                ('client_address', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_username', models.CharField(max_length=50)),
                ('employee_password', models.CharField(max_length=50)),
                ('employee_phone', models.CharField(max_length=30)),
                ('employee_email', models.CharField(max_length=30)),
                ('employee_state', models.CharField(max_length=30)),
                ('employee_district', models.CharField(max_length=30)),
                ('employee_zipcode', models.CharField(max_length=30)),
                ('employee_address', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('catagory', models.CharField(max_length=50)),
                ('priceper_head', models.IntegerField()),
                ('priceper_kg', models.IntegerField()),
                ('food_deatails', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
