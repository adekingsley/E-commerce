# Generated by Django 4.2.1 on 2023-06-27 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0009_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='First_name',
        ),
        migrations.DeleteModel(
            name='Orderitems',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='block.customer'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(blank=True, to='block.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='block.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='block.product'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='block.cart'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
