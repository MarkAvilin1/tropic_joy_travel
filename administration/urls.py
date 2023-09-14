from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import AdminSitemap
from . import views

sitemaps = {
    'admin': AdminSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # English
    path('', views.index, name='home'),
    path('en/contact', views.contact, name='contact_en'),
    # Arabic
    path('ar/home', views.index_ar, name='home_ar'),
    path('ar/contact', views.contact_ar, name='contact_ar'),
    # Russian
    path('ru/home', views.index_ru, name='home_ru'),
    path('ru/contact', views.contact_ru, name='contact_ru'),
]
