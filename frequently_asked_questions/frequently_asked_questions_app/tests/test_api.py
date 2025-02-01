import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from frequently_asked_questions_app.models import FAQ


@pytest.mark.django_db
def test_faq_list_empty():
    client = APIClient()
    url = reverse("faq-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_faq_list_with_data():
    FAQ.objects.create(
        question="What is Django?",
        answer="A Python web framework."
    )
    FAQ.objects.create(
        question="What is Python?",
        answer="A programming language."
    )

    client = APIClient()
    url = reverse("faq-list")
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["question"] == "What is Django?"
    assert data[1]["answer"] == "A programming language."


@pytest.mark.django_db
def test_faq_list_in_hindi():
    FAQ.objects.create(
        question="Hello?",
        answer="World!",
        question_hi="नमस्ते?",
        answer_hi="दुनिया!"
    )

    client = APIClient()
    url = reverse("faq-list")
    response = client.get(f"{url}?lang=hi")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    faq_item = data[0]
    assert faq_item["question"] == "नमस्ते?"
    assert faq_item["answer"] == "दुनिया!"
