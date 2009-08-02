from django.conf import settings


USE_TAGS = getattr(settings, 'LOGOS_USE_TAGS', False)
