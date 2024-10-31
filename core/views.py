from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from core.forms import UserRegistrationForm
from django.views import View

class FirstView(View):
    def Rec(request: HttpRequest) -> HttpResponse:
        return HttpResponse('Hello world!')

class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_form = UserRegistrationForm()
        return render(request, 'WebsiteHTMLs/register.html', {'user_form': user_form})

    def post(self, request: HttpRequest) -> HttpResponse:
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'WebsiteHTMLs/register_done.html', {'new_user': new_user})
        return render(request, 'WebsiteHTMLs/register.html', {'user_form': user_form})