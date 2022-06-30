from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return self.name

    def quiz_count(self):
        return self.quizzes.count()

class Quiz(models.Model):
    """
    Quiz model
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=100, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def question_count(self):
        return self.questions.count()
        
        

class Question(models.Model):
    """
    Question model
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200, primary_key=True)
    difficulty = models.IntegerField(default=1, choices=((1, 'Easy'), (2, 'Medium'), (3, 'Hard')))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    """
    Answer model
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200)
    is_right = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_text