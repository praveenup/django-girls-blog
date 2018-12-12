from django.contrib import admin
from .models import Question, Answers, Choice

admin.site.register(Question)
admin.site.register(Choice)  
admin.site.register(Answers) 
