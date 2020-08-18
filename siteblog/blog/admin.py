from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class HomeFirstScreenInline(admin.StackedInline):
    model = HomeFirstScreen


class HomeSecondScreenInline(admin.StackedInline):
    model = HomeSecondScreen


class HomeStepWorkInline(admin.StackedInline):
    model = HomeStepWork


class HomeReviewsInline(admin.StackedInline):
    model = HomeReviews


class HomePartnersInline(admin.StackedInline):
    model = HomePartners


class HomeQuestionsInline(admin.StackedInline):
    model = HomeQuestions


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
