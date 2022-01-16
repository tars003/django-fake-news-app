from django.contrib import admin
from django.urls import path
from fake_news import views
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fake_news, name='fake_news'),
]

