import openai
from django.conf import settings

openai.api_key = settings.OPEN_AI_API_KEY
