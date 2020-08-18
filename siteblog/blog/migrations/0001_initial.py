# Generated by Django 3.1 on 2020-08-09 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField(blank=True, verbose_name='Ответ')),
            ],
        ),
        migrations.CreateModel(
            name='HomeFirstScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Офер')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фон офера')),
            ],
        ),
        migrations.CreateModel(
            name='HomePartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото партнера')),
            ],
        ),
        migrations.CreateModel(
            name='HomeQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255, verbose_name='Вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='HomeReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка отзыва')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeSecondScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок компании')),
                ('description', models.TextField(blank=True, verbose_name='описание компнании')),
            ],
        ),
        migrations.CreateModel(
            name='HomeStepWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название шага')),
                ('description', models.TextField(blank=True, verbose_name='Описание шага')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка шага')),
                ('title2', models.CharField(max_length=255, verbose_name='Название шага')),
                ('description2', models.TextField(blank=True, verbose_name='Описание шага')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка шага')),
                ('title3', models.CharField(max_length=255, verbose_name='Название шага')),
                ('description3', models.TextField(blank=True, verbose_name='Описание шага')),
                ('photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка шага')),
                ('title4', models.CharField(max_length=255, verbose_name='Название шага')),
                ('description4', models.TextField(blank=True, verbose_name='Описание шага')),
                ('photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка шага')),
                ('title5', models.CharField(max_length=255, verbose_name='Название шага')),
                ('description5', models.TextField(blank=True, verbose_name='Описание шага')),
                ('photo5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка шага')),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('home_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homeanswer')),
                ('home_first_screen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homefirstscreen')),
                ('home_partners', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homepartners')),
                ('home_questions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homequestions')),
                ('home_reviews', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homereviews')),
                ('home_second_scree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homesecondscreen')),
                ('home_step_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homestepwork')),
            ],
        ),
        migrations.AddField(
            model_name='homeanswer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.homequestions'),
        ),
    ]