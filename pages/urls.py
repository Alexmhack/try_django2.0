from django.contrib import admin
from django.urls import path

from .views import (
	homepage_view,
	contact_view,
	about_view
)


app_name = 'pages'

urlpatterns = [
    path('', homepage_view, name='home_view'),
    path('about/', about_view, name='home_view'),
    path('contact/', contact_view, name='home_view'),
]