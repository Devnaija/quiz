from django.shortcuts import render
from .models import Question
# Create your views here.


def index(request):
    questions = Question.objects.all()

    if request.method == "POST":
        score = 0

        for question in questions:
            answer = request.POST.get(str(question.id))

            if answer == question.answer:
                score += 1

        return render(request, 'result.html', {'score': score, 'total': len(questions)})
    return render(request, 'index.html', {'questions': questions})
