from rest_framework import serializers

from quiz.models import Answer, Category, Question, Quiz

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', "quiz_count")

class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quiz
        fields = ( "title", "question_count")
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("answer_text", "is_right")

class QuestionSerializer(serializers.ModelSerializer):
    answers=AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ("title", "difficulty", "answers")

