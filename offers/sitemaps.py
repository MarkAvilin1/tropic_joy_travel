from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class OffersSitemap(Sitemap):
    priority = 0.9
    changefreq = 'never'

    def items(self):
        return ['trips', 'other', 'pickup', 'city', 'safari', 'kawasan', 'hopping', 'trips_ar', 'other_ar', 'pickup_ar',
                'city_ar', 'safari_ar', 'kawasan_ar', 'hopping_ar', 'trips_ru', 'other_ru', 'pickup_ru',
                'city_ru', 'safari_ru', 'kawasan_ru', 'hopping_ru']

    def location(self, item):
        return reverse(item)
