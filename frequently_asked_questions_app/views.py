# frequently_asked_questions_app/views.py
from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer


class FAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get("lang", "en")
        cache_key = f"faqs_{lang}"

        # Attempt to fetch from cache
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        # Otherwise fetch from DB, serialize
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset, many=True, context={"lang": lang})
        data = serializer.data

        # Cache data for 5 minutes
        cache.set(cache_key, data, 60 * 5)
        return Response(data)
