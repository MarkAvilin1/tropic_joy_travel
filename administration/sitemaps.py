from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class AdminSitemap(Sitemap):
    priority = 0.9
    changefreq = 'never'

    def items(self):
        return ['home', 'contact', 'home_ar', 'contact_ar', 'home_ur', 'contact_ur']

    def location(self, item):
        return reverse(item)
