from rest_framework import serializers
from link_editor_app.models import Logic

class LogicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logic
        fields = '__all__'