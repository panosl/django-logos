from django.conf import settings


USE_TAGS = getattr(settings, 'LOGOS_USE_TAGS', True)
TAGS_PAGINATE_BY = getattr(settings, 'LOGOS_TAGS_PAGINATE_BY', 10)
NUM_LATEST = getattr(settings, 'LOGOS_NUM_LATEST', 100)
