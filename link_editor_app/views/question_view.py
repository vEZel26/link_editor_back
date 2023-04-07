from rest_framework.viewsets import ModelViewSet
from link_editor_app.serializers import QuestionSerializer
from link_editor_app.models import Question

class QuestionViewSet(ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all().order_by('id')