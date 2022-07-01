from django.shortcuts import render
from quiz.models import Category, Question, Quiz
from rest_framework.response import Response
from rest_framework.decorators import action
from quiz.serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from  rest_framework.generics import ListCreateAPIView

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
    
class QuizMVS(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    # @action(detail=True, methods=['get'])
    # def get_quiz_by_category(self, request, *args, **kwargs):
    #     category = request.query_params.get('category')
    #     if category:
    #         queryset = Quiz.objects.filter(category=category)
    #     else:
    #         queryset = Quiz.objects.all()
    #     serializer = QuizSerializer(queryset, many=True)
    #     return Response(serializer.data)

class QuestionMVS(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuizListCreateView(ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        if category:
            return Quiz.objects.filter(category=category)
        return Quiz.objects.all()

class QuestionListCreateView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser ,)

    def get_queryset(self):
        quiz = self.kwargs['quiz']
        if quiz:
            return Question.objects.filter(quiz=quiz)
        return Question.objects.all()

