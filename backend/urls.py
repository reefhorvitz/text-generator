from django.urls import path

from backend.views.text_generator import TextGeneratorView

urlpatterns = [
    path('generate-text/', TextGeneratorView.as_view()),
]
