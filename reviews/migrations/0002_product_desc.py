# Generated by Django 2.0.4 on 2018-04-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default='Please add a description'),
        ),
    ]
