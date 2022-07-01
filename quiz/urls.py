from django.urls import path, re_path
from rest_framework import routers
from quiz.views import CategoryViewSet, QuestionListCreateView, QuestionMVS, QuizListCreateView, QuizMVS


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'quiz', QuizMVS)
router.register(r'question', QuestionMVS)


urlpatterns = [
    path('<str:category>', QuizListCreateView.as_view()),
    path('<str:category>/<str:quiz>', QuestionListCreateView.as_view()),
]

urlpatterns += router.urls
