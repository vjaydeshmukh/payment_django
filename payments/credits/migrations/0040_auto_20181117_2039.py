# Generated by Django 2.1.2 on 2018-11-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0039_auto_20181117_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='248B3FFE20F2', max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='F3324432F1E8', max_length=14, unique=True),
        ),
    ]
