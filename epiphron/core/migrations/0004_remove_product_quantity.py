# Generated by Django 2.1.7 on 2019-04-30 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190501_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
