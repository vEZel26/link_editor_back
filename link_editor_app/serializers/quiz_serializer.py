from rest_framework import serializers
from link_editor_app.models import Quiz
from link_editor_app.serializers import QuestionSerializer

class QuizSerializer(serializers.ModelSerializer):

    question = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Quiz
        fields = '__all__'