# Generated by Django 2.2 on 2021-07-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='mainapp.Color'),
        ),
    ]
