from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from core.forms import UserLoginForm, UserRegistrationForm


class FirstView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'core/first_page.html')


class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_form = UserRegistrationForm()
        return render(request, 'core/register.html', {'user_form': user_form})

    def post(self, request: HttpRequest) -> HttpResponse:
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'core/register_done.html', {'new_user': new_user})
        return render(request, 'core/register.html', {'user_form': user_form})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_form = UserLoginForm()
        return render(request, 'core/login.html', {'user_form': user_form})

    def post(self, request: HttpRequest) -> HttpResponse:
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('core/first_page.html') доделать и исправить
                return render(request, 'core/first_page.html', {'user_form': user_form})
            else:
                user_form.add_error(None, 'Invalid username or password.')

        return render(request, 'core/login.html', {'user_form': user_form})
