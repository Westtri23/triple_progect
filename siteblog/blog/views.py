from django.views.generic import ListView
from blog.models import *


class HomePage(ListView):
    model = HomePage
    template_name = 'blog/index.html'
    context_object_name = 'homepage'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_screen'] = HomeFirstScreen.objects.all()
        context['second_screen'] = HomeSecondScreen.objects.all()
        context['step_work'] = HomeStepWork.objects.all()
        context['reviews'] = HomeReviews.objects.all()
        context['partners'] = HomePartners.objects.all()
        context['questions'] = HomeQuestions.objects.all()
        context['category'] = ServicesCategory.objects.all()
        context['keys'] = KeysPage.objects. \
            prefetch_related('category') \
            .only('title', 'slug', 'description', 'photo_keys_home', 'category__title', 'category__slug', )
        context['service'] = ServicesPage.objects \
            .prefetch_related('category') \
            .only('title', 'slug', 'description_services', 'photo_services'\
                  , 'category', 'category__title', 'category__slug', )
        return context


class ServicesByCategory(ListView):
    template_name = 'service_category/index.html'
    context_object_name = 'cat'

    def get_queryset(self):
        return ServicesPage.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = ServicesPage.objects.all()
        context['name_page'] = ServicesCategory.objects \
            .filter(slug=self.kwargs['slug'])
        context['next_category'] = ServicesCategory.objects. \
            exclude(slug=self.kwargs['slug'])
        return context


class ServicesPageView(ListView):
    template_name = 'services/index.html'
    context_object_name = 'service_item'

    def get_queryset(self):
        return ServicesPage.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = ServicesPage.objects.all()
        context['slider'] = ServicesPageSlider.objects.all()
        context['benefit'] = ServicesPageBenefit.objects.all()
        return context


class KeysPageView(ListView):
    model = KeysPage
    template_name = 'keys/index.html'
    context_object_name = 'keys'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = ServicesPage.objects.all()
        return context


class KeysPageItemView(ListView):
    template_name = 'keys/item.html'
    context_object_name = 'keys_item'

    def get_queryset(self):
        return KeysPage.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = ServicesPage.objects.all()
        context['category'] = ServicesCategory.objects.all()
        context['slider'] = KeysPageSlider.objects.all()
        context['keys'] = KeysPage.objects.exclude(slug=self.kwargs['slug'])
        return context



