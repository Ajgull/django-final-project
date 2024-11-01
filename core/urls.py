from django.contrib import admin
from django.urls import path

from core.views import FirstView, LoginView, RegisterView

urlpatterns = [
  path('', FirstView.as_view()),
  path('admin/', admin.site.urls),
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
]
