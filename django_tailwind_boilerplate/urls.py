from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
]
