from .models import Question
from django import forms

class QuizForm(forms.ModelForm):

    class Meta:
        CHOICES = (
            ('1', "Question.option1"),
            ('2', "Question.option2"),
            ('3', "Question.option3"),
            ('4', "Question.option4"),
        )
        model =  Question
        answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
        fields = ('question','answer')

