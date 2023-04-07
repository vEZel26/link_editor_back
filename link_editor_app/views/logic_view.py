from rest_framework.viewsets import ModelViewSet
from link_editor_app.serializers import LogicSerializer
from link_editor_app.models import Logic

class LogicViewSet(ModelViewSet):

    serializer_class = LogicSerializer
    queryset = Logic.objects.all()