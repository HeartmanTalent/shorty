from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Short(models.Model):
    long_url = models.URLField(_("Long URL"), null=False)
    short_url = models.CharField(_("Short URL"), max_length=50, null=False)
    user = models.ForeignKey(
        User, blank=True, null=True, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.short_url)

    class Meta(object):
        unique_together = [['long_url', 'user']]


class Visit(models.Model):
    referrer = models.URLField(_("Referrer"))
    date_visited = models.DateTimeField(
        "Date Visited ", null=False, blank=False, unique=False, auto_now_add=True)
    country = models.CharField(_("Country"), max_length=50, null=True)
    device = models.CharField(_("Device"), max_length=50, null=True)
    browser = models.CharField(_("Browser"), max_length=50, null=True)
    short = models.ForeignKey(
        'Short', blank=False, null=True, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
# social media signup
# simple style
