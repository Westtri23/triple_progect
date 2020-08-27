from contact_form.forms import HomePageMainForm
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def contactView(request):
    if request.method == 'POST':
        form = HomePageMainForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['ВАШ_EMAIL_ДЛЯ_ПОЛУЧЕНИЯ_СООБЩЕНИЯ']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'site/thanks.html')
    else:
        # Заполняем форму
        form = HomePageMainForm()
    # Отправляем форму на страницу
    return render(request, 'blog/templates/blog/index.html', {'form': form})
