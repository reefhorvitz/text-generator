from rest_framework.generics import CreateAPIView

from backend.serializers.text_generator import TextGeneratorSerializer


class TextGeneratorView(CreateAPIView):
    serializer_class = TextGeneratorSerializer
