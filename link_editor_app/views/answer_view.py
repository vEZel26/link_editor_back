from rest_framework.viewsets import ModelViewSet
from link_editor_app.serializers import AnswerSerializer
from link_editor_app.models import Answer

class AnswerViewSet(ModelViewSet):

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()