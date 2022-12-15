from rest_framework import serializers

from backend.service.text_generator import generate_text


class TextGeneratorSerializer(serializers.Serializer):
    command = serializers.CharField(write_only=True)
    response = serializers.CharField(read_only=True)

    def create(self, validated_data):
        command = validated_data.get("command")
        response = generate_text(command)
        return {"response": response}
