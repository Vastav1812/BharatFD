# frequently_asked_questions_app/admin.py
from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at", "updated_at")
    search_fields = ("question", "question_hi", "question_bn")
    list_filter = ("created_at", "updated_at")
