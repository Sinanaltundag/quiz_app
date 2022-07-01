from rest_framework import serializers

from quiz.models import Answer, Category, Question, Quiz

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', "quiz_count")

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("answer_text", "is_right")

class QuestionSerializer(serializers.ModelSerializer):
    answers=AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ("title", "difficulty", "answers")




class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ( "title", "question_count", "category", "questions")

    def create(self, validated_data):
        print(validated_data)
        questions = validated_data.pop('questions')

        quiz = Quiz.objects.create(**validated_data)
        for question in questions:
            answers = question.pop('answers')
            Question.objects.create(quiz=quiz, **question)
            for answer in answers:
                # Question.objects.filter(pk=question.get('pk')).first().answers.create(**answer)
                # Answer.objects.create(question=Question.objects.filter(pk=question.get('pk')).first(), **answer)
                answer.question_title = question["title"]
                Answer.objects.create(question=question, **answer)
        return quiz