# Generated by Django 3.0.2 on 2020-05-02 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200502_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='superCategory_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.SuperCategory'),
        ),
    ]
