from django.contrib.auth.models import User
from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    is_ready_to_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "quizzes"
class Question(models.Model):
    text = models.CharField(max_length=225)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Answer(models.Model):
    translation = models.CharField(max_length=225)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)

    def __str__(self):
        return self.translation

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Вы, {self.user.username}, перевели {self.question.text} как {self.answer.translation}."



