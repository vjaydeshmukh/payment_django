# Generated by Django 2.1.2 on 2018-11-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0007_auto_20181105_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='key',
            field=models.CharField(default='epxu%rio4|LU_0GcDwu', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='GSG1UD73r34E', max_length=14, unique=True),
        ),
    ]
