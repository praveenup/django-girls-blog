from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice, Answers


def index(request):
    latest_question_list = Question.objects.all()
    answered =[]
    for ques in latest_question_list:
        choices = ques.choice_set.all()
        f=False
        for c in choices:
            ans = Answers.objects.filter(choice=c, user=request.user).count()
            if ans==1:
                f=True
                break
        if f==True:
            answered.append(True)
            print("true",ques.id)
        else:
            answered.append(False)
            print("false",ques.id)
            
        
    context = {
        'latest_question_list': latest_question_list,
        'answered' : answered
    }
    return render(request, 'mcq/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    c = Question.objects.count()
    count = range(1,c+1)
    p = question_id-1
    q = question_id+1
    return render(request, 'mcq/detail.html', {'question': question,'count':count,'c':c,'p':p,'q':q})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mcq/result.html', {'question': question})

def mark(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
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
        return HttpResponseRedirect(reverse('mcq:detail', args=(question.id,)))

def submission(request):
    ans = Answers.objects.filter(user=request.user)
    c=0
    for a in ans :
        if a.correct == True:
            c=c+1
    return HttpResponse(c)

    