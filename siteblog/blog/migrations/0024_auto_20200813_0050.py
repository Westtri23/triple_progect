# Generated by Django 3.1 on 2020-08-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200812_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyspage',
            name='photo_home',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото на главную'),
        ),
        migrations.AddField(
            model_name='keyspage',
            name='photo_keys',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото на кейсы'),
        ),
    ]