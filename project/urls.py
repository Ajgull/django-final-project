from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import FirstView, RegisterView
from django.contrib import admin

urlpatterns = [
  path('', FirstView.as_view()),
  path('admin/', admin.site.urls),
  path('register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
