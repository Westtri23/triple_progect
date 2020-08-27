from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class HomeFirstScreenInline(admin.StackedInline):
    model = HomeFirstScreen
    extra = 0


class HomeSecondScreenInline(admin.StackedInline):
    model = HomeSecondScreen
    extra = 0


class HomeStepWorkInline(admin.StackedInline):
    model = HomeStepWork
    extra = 0


class HomeReviewsInline(admin.StackedInline):
    model = HomeReviews
    extra = 0


class HomePartnersInline(admin.StackedInline):
    model = HomePartners
    extra = 0


class HomeQuestionsInline(admin.StackedInline):
    model = HomeQuestions
    extra = 0


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = [
        HomeFirstScreenInline,
        HomeSecondScreenInline,
        HomeStepWorkInline,
        HomeReviewsInline,
        HomePartnersInline,
        HomeQuestionsInline,
    ]


class ServicesPageSliderInline(admin.StackedInline):
    model = ServicesPageSlider


class ServicesPageBenefitInline(admin.StackedInline):
    model = ServicesPageBenefit


@admin.register(ServicesCategory)
class ServicesCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {
            'fields': ('title', 'slug', 'description', 'services_icon', 'services_photo',)
        })
    ]


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    model = ServicesPage


@admin.register(ServicesPage)
class ServicesPageAdmin(admin.ModelAdmin):
    inlines = [
        ServicesPageSliderInline,
        ServicesPageBenefitInline
    ]
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm


class KeysPageSliderInline(admin.StackedInline):
    model = KeysPageSlider


@admin.register(KeysPage)
class KeysPageAdmin(admin.ModelAdmin):
    inlines = [
        KeysPageSliderInline,
    ]
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
