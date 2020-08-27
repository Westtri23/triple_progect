from django import forms


class HomePageMainForm(forms.Form):
    hidden = forms.CharField(widget=forms.HiddenInput(attrs={'name': 'act', 'value': 'seo'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'service-form__input border-input', 'name': 'site',
                                                         'placeholder': 'Ваше имя'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'service-form__input border-input phone_mask',
                                                            'name': 'tel', 'placeholder': 'Ваше номер'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'slider', 'type': 'range', 'id': 'slider',
                                                               'min': '0', 'max': '100', "value": '100'}))
    politic = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'service-form__checkbox',
                                                                'checked': 'checked', 'name': 'pdn',
                                                                'id': "service_pdn1"}), initial=True)
