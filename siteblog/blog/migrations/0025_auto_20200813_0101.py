# Generated by Django 3.1 on 2020-08-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200813_0050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyspage',
            options={'verbose_name': 'Кейс', 'verbose_name_plural': 'Кейсы'},
        ),
        migrations.AlterModelOptions(
            name='keyspageslider',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайдер'},
        ),
        migrations.AddField(
            model_name='keyspage',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Краткое описание'),
        ),
    ]
