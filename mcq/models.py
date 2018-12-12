from django.db import models
from django.conf import settings
from django.urls import reverse

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.id , self.question_text    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Answers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default="", on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    def __str__(self):
        return self.user, self.choice, self.correct
    
