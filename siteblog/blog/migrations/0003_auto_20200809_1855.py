# Generated by Django 3.1 on 2020-08-09 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200809_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homereviews',
            name='link',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homeanswer'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_first_screen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homefirstscreen'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_partners',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homepartners'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homequestions'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homereviews'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_second_scree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homesecondscreen'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_step_work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homestepwork'),
        ),
    ]
