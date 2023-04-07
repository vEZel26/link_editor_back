from rest_framework import serializers
from link_editor_app.models import Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'