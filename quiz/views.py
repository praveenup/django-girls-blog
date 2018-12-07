from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question

@login_required
def main(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'quiz/main.html', {'question': question})
    

# def quiz(request):
#     form = QuizForm()
#     return render(request, 'quiz/quiz.html', {'form': form})
