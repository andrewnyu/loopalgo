from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='interview/', permanent=True)),
    path('admin/', admin.site.urls),
    path('interview/', include('interview.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]