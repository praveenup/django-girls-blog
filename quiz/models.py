from django.db import models
from django.conf import settings

class Question(models.Model):
    question = models.TextField(default="")
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()  
    answer = models.TextField()    

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.question