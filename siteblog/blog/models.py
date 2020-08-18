from django.db import models

'''
Home page
===========
Title
-----------------

*First screen
......................
Title, photo

*Second screen
......................
Title, description

*step work
......................
Title, description, photo

*reviews
......................
photo, link


*partners
......................
photo, 

*answer, question
......................
answer, question 

'''


class HomeFirstScreen(models.Model):
    objects = None
    home_first_screen = models.ForeignKey('HomePage', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255, verbose_name='Офер')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фон офера', null=True)

    class Meta:
        verbose_name = 'Первыйый скрин'
        verbose_name_plural = 'Первыйый скрин'

    def __str__(self):
        return self.title


class HomeSecondScreen(models.Model):
    objects = None
    home_second_scree = models.ForeignKey('HomePage', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок компании')
    description = models.TextField(verbose_name='описание компнании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Второй скрин'
        verbose_name_plural = 'Второй скрин'


class HomeStepWork(models.Model):
    objects = None
    home_step_work = models.ForeignKey('HomePage', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255, verbose_name='Название шага', null=True)
    description = models.TextField(verbose_name='Описание шага', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка шага', null=True)
    title2 = models.CharField(max_length=255, verbose_name='Название шага', null=True)
    description2 = models.TextField(verbose_name='Описание шага', null=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка шага', null=True)
    title3 = models.CharField(max_length=255, verbose_name='Название шага', null=True)
    description3 = models.TextField(verbose_name='Описание шага', null=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка шага', null=True)
    title4 = models.CharField(max_length=255, verbose_name='Название шага', null=True)
    description4 = models.TextField(verbose_name='Описание шага', null=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка шага', null=True)
    title5 = models.CharField(max_length=255, verbose_name='Название шага', null=True)
    description5 = models.TextField(verbose_name='Описание шага', null=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка шага', null=True)
    title6 = models.CharField(max_length=255, verbose_name='Название шага', null=True)
    description6 = models.TextField(verbose_name='Описание шага', null=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Картинка шага', null=True)

    class Meta:
        verbose_name = 'Как мы работаем'
        verbose_name_plural = 'Как мы работаем'


class HomeReviews(models.Model):
    objects = None
    home_reviews = models.ForeignKey('HomePage', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Картинка отзыва', null=True)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class HomePartners(models.Model):
    objects = None
    home_partners = models.ForeignKey('HomePage', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото партнера', null=True)

    class Meta:
        verbose_name = 'Наши партнеры'
        verbose_name_plural = 'Наши партнеры'


class HomeQuestions(models.Model):
    objects = None
    home_questions = models.ForeignKey('HomePage', on_delete=models.PROTECT, null=True)
    answer = models.CharField(max_length=255, verbose_name='Вопрос')
    questions = models.TextField(blank=True, verbose_name='Ответ')

    def __str__(self):
        return '{}/{}'.format(self.answer, self.questions, )

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class HomePage(models.Model):
    title = models.CharField(max_length=255)
    objects = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главную'
        verbose_name_plural = 'Главная'


'''
Services page
==============================
Title, Slug, Money , Time
------------------------------

*Slider
..............................
Photo

*RightSideBarBenefit
..............................
text

*ServicesCategory
.............................
title, slug, description, home_icon, services_photo 
    

'''


class ServicesPageSlider(models.Model):
    objects = None
    object = None
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото слайдера', blank=True)
    services_page = models.ForeignKey('ServicesPage', on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'


class ServicesPageBenefit(models.Model):
    objects = None
    text = models.CharField(max_length=255)
    services_page = models.ForeignKey('ServicesPage', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Выгода'
        verbose_name_plural = 'Выгода'


class ServicesCategory(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url')
    description = models.CharField(max_length=255)
    services_icon = models.FileField(upload_to='photos/%Y/%m/%d', verbose_name='Иконка главная', blank=True)
    services_photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Иконка услуг', blank=True)
    home_services_category = models.ForeignKey(HomePage, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class ServicesPage(models.Model):
    objects: None
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url')
    description_services = models.CharField(max_length=255, verbose_name='Описание на категорию', blank=True)
    photo_services = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото на категорию', blank=True)
    money = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.ManyToManyField(ServicesCategory)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'


'''
KEYS Page
==============================
Title, Slug, Content , Category
------------------------------

*Slider
..............................
Photo

'''


class KeysPage(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url')
    description = models.CharField(max_length=255, verbose_name='Краткое описание', blank=True)
    content = models.TextField(blank=True)
    category = models.ManyToManyField(ServicesCategory)
    photo_keys_home = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото на главную', blank=True)
    photo_keys = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото на кейсы', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'


class KeysPageSlider(models.Model):
    objects = None
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото слайдера', blank=True)
    keys_page = models.ForeignKey(KeysPage, on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'
