from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Short(models.Model):
    long_url = models.URLField(_("Long URL"), null=False)
    short_url = models.TextField(_("Short URL"), null=False)
    user = models.ForeignKey(
        User, blank=True, null=True, unique=False, on_delete=models.CASCADE)


class Visit(models.Model):
    referrer = models.URLField(_("Referrer"))
    date_visited = models.DateTimeField(
        "Date Visited ", null=False, blank=False, unique=False, auto_now_add=True)
    country = models.CharField(_("Country"), max_length=50, null=True)
    device = models.CharField(_("Device"), max_length=50, null=True)
    browser = models.CharField(_("Browser"), max_length=50, null=True)
    short = models.ForeignKey(
        'Short', blank=False, null=True, unique=False, on_delete=models.CASCADE)

# social media signup
# simple style