from django.core.cache import cache

from diary.models import Diary
from config.settings import CACHE_ENABLED


def get_articles_from_cache():

    if not CACHE_ENABLED:
        return Diary.objects.all()
    else:
        key = 'diary'
        cache_data = cache.get(key)
        if cache_data is not None:
            return cache_data
        else:
            cache_data = Diary.objects.all()
            cache.set(key, cache_data)
            return cache_data
