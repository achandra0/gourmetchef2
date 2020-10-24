# Generated by Django 2.1.5 on 2020-10-23 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='prod_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='products.Product'),
            preserve_default=False,
        ),
    ]