import random
import string

from django.conf import settings

CHAR_CHOICES = string.ascii_letters + string.digits


def generate_random_string(length=settings.SHORTIFY_SLUG_LENGTH):
    return "".join(random.SystemRandom().choice(CHAR_CHOICES) for _ in range(length))
