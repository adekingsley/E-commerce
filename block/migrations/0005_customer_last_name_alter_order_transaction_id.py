# Generated by Django 4.2 on 2023-05-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]