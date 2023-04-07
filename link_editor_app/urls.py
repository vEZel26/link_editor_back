from rest_framework import routers
from django.urls import path, include

from link_editor_app.views import (
    QuizViewSet,
    LogicViewSet,
    QuestionViewSet,
    AnswerViewSet
)

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'quiz', QuizViewSet, basename='quiz')
router.register(r'logic', LogicViewSet, basename='logic')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'answer', AnswerViewSet, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
    * router.urls,
]
