# Generated by Django 2.1.2 on 2018-11-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0018_auto_20181107_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='key',
            field=models.CharField(default='177014', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='24150B8FC7', max_length=14, unique=True),
        ),
    ]
