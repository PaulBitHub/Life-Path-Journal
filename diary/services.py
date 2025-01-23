from django.core.cache import cache
from django.db.models import QuerySet

from diary.models import Diary
from config.settings import CACHE_ENABLED


# def get_articles_from_cache():
#
#     if not CACHE_ENABLED:
#         return Diary.objects.all()
#     else:
#         key = "diary"
#         cache_data = cache.get(key)
#         if cache_data is not None:
#             return cache_data
#         else:
#             cache_data = Diary.objects.all()
#             cache.set(key, cache_data)
#             return cache_data


def get_articles_from_cache(user_id: int = 0) -> QuerySet[Diary]:
    qs = Diary.objects.all()
    if user_id:
        qs = qs.filter(owner_id=user_id)

    if not CACHE_ENABLED:
        return qs

    key = f"diary:{user_id}"
    cache_data = cache.get(key)
    if cache_data is not None:
        return cache_data

    cache.set(key, qs)
    return qs
