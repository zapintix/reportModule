from django.contrib import admin
from django.urls import path, include

from otchet.views import ReportCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/reports/', ReportCreateView.as_view(), name='report-create'),
]
