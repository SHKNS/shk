from django.contrib import admin
from django.urls import include, path

from test_app import views

app_name = 'test_app'

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
]