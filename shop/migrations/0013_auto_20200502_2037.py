# Generated by Django 3.0.2 on 2020-05-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200502_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(default='', max_length=200),
        ),
    ]
