# Generated by Django 2.2 on 2021-07-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('name', models.CharField(max_length=180, verbose_name='Название')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
            ],
        ),
    ]
