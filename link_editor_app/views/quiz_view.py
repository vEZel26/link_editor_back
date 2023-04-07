from rest_framework.viewsets import ModelViewSet
from link_editor_app.serializers import QuizSerializer
from link_editor_app.models import Quiz

class QuizViewSet(ModelViewSet):

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all().order_by('id')