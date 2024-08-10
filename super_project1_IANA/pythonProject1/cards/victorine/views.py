from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    quizzes = Quiz.objects.all()
    print(quizzes)
    context = {"quizzes": quizzes, }
    return render(request, "index.html", context=context)

def quiz_list(request):
    quizzes = Quiz.objects.all()
    print(quizzes)
    print("asasdasd")
    context = {"quizzes": quizzes, }
    return render(request, "quiz_list.html", context=context)

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = quiz.questions.all()
    context = {"quiz": quiz, "questions": question}
    return render(request, "card.html", context)

def answer_detail(request, answer_id):
    question = get_object_or_404(Question, id=answer_id)
    answer = question.answers.all()
    context = {"question": question, "answer": answer}
    return render(request, "card.html", context)

