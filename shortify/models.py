from django.conf import settings
from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel

from .utils import generate_random_string


class ShortifyURL(TimeStampedModel):
    url = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, default=generate_random_string)
    hits = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("shortify:detail", kwargs={"slug": self.slug})

    def get_redirect_url(self):
        return reverse("shortify-redirect", kwargs={"slug": self.slug})
