# Generated by Django 4.2 on 2023-05-12 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0005_customer_last_name_alter_order_transaction_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Products',
        ),
    ]
