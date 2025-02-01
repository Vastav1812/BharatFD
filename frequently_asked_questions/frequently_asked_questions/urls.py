# frequently_asked_questions/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("frequently_asked_questions_app.urls")),
]
