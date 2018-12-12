from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice, Answers


def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'mcq/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mcq/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # ques= ques.first()
    # ques = ques.question_text
    # ans = ques.answer_text
    # choices = ans.choice_set.all()


    # ans.choice
    # if  ans == question.answer_text:
    #     print(ans)
    # else:
    #     print(ans.choice)

    return render(request, 'mcq/result.html', {'question': question})

def mark(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'mcq/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        ans = question.answer_text
        ch = selected_choice.choice_text
        print(ans, ch)
        temp = False
        if ch == ans :
            temp = True
        ch_set = question.choice_set.all()
        f=False
        ans_obj =Answers()
        for c in ch_set:
            try:
                ans_obj = Answers.objects.get(user= request.user ,choice = c)
            except(KeyError, Answers.DoesNotExist):
                f=False
            else:
                f=True
                break
        if f==True:
            ans_obj.choice=selected_choice
            ans_obj.correct=temp
            ans_obj.save()
        else:
            ans = Answers(user=request.user, choice = selected_choice, correct=temp)
            ans.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mcq:results', args=(question.id,)))

def submission(request):
    ans = Answers.objects.filter(user=request.user)
    c=0
    for a in ans :
        if a.correct == True:
            c=c+1
    return HttpResponse(c)

    