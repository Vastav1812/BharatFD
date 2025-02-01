import pytest
from frequently_asked_questions_app.models import FAQ


@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="Q1?", answer="A1.")
    assert faq.pk is not None
    assert faq.question == "Q1?"
    assert faq.answer == "A1."


@pytest.mark.django_db
def test_faq_str_method():
    faq = FAQ.objects.create(
        question="What is your name?",
        answer="My name is Django FAQ System!"
    )
    assert str(faq).startswith("What is your name?")


@pytest.mark.django_db
def test_get_translated_question_and_answer():
    faq = FAQ.objects.create(
        question="Hello?",
        answer="World!",
        question_hi="नमस्ते?",
        answer_hi="दुनिया!"
    )
    assert faq.get_translated_question() == "Hello?"
    assert faq.get_translated_answer() == "World!"
    assert faq.get_translated_question(lang="hi") == "नमस्ते?"
    assert faq.get_translated_answer(lang="hi") == "दुनिया!"
    assert faq.get_translated_question(lang="bn") == "হ্যালো?"
    assert faq.get_translated_answer(lang="bn") == "বিশ্ব!"


@pytest.mark.django_db
def test_auto_translation_on_save():
    faq = FAQ.objects.create(question="Hi", answer="Welcome")
    assert faq.question_hi is not None
    assert faq.answer_hi is not None
