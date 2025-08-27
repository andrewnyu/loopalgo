from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path(settings.ADMIN_URL, admin.site.urls),
    path('interview/', include('interview.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]