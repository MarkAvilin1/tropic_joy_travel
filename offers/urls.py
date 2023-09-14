from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import OffersSitemap
from . import views

sitemaps = {
    'offers': OffersSitemap,
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # English
    path('en/trips/', views.trips, name='trips_en'),
    path('en/other/', views.other, name='other_en'),
    path('en/pickup/', views.pickup, name='pickup_en'),
    path('en/city/', views.city, name='city_en'),
    path('en/kawasan/', views.kawasan, name='kawasan_en'),
    path('en/safari/', views.safari, name='safari_en'),
    path('en/hopping/', views.hopping, name='hopping_en'),
    # Arabic
    path('ar/trips/', views.trips_ar, name='trips_ar'),
    path('ar/other/', views.other_ar, name='other_ar'),
    path('ar/pickup/', views.pickup_ar, name='pickup_ar'),
    path('ar/city/', views.city_ar, name='city_ar'),
    path('ar/kawasan/', views.kawasan_ar, name='kawasan_ar'),
    path('ar/safari/', views.safari_ar, name='safari_ar'),
    path('ar/hopping/', views.hopping_ar, name='hopping_ar'),
    # Russian
    path('ru/trips/', views.trips_ru, name='trips_ru'),
    path('ru/other/', views.other_ru, name='other_ru'),
    path('ru/pickup/', views.pickup_ru, name='pickup_ru'),
    path('ru/city/', views.city_ru, name='city_ar'),
    path('ru/kawasan/', views.kawasan_ru, name='kawasan_ru'),
    path('ru/safari/', views.safari_ru, name='safari_ru'),
    path('ru/hopping/', views.hopping_ru, name='hopping_ru'),
]
