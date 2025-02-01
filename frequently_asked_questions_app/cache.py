from django.core.cache import cache
from functools import wraps


def cache_translation(timeout=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(self, field_name, lang):
            cache_key = f'faq_{self.id}_{field_name}_{lang}'
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            result = func(self, field_name, lang)
            cache.set(cache_key, result, timeout)
            return result
        return wrapper
    return decorator
