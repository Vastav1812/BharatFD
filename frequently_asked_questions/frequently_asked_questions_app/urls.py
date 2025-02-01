# frequently_asked_questions_app/urls.py
from django.urls import path
from .views import FAQListAPIView

urlpatterns = [
    path("faqs/", FAQListAPIView.as_view(), name="faq-list"),
]
