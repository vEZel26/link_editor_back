from rest_framework import serializers
from link_editor_app.models import Question
from link_editor_app.serializers import AnswerSerializer, LogicSerializer

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True, many=True)
    logic = LogicSerializer(read_only=True, many=True)


    class Meta:
        model = Question
        fields = '__all__'