from django.urls import path

from . import views
app_name = 'mcq'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'), # all question here
    path('<int:question_id>/', views.detail, name='detail'), # Q. detail per page 1 question
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/mark/', views.mark, name='mark'), #mark answer
    path('submission/', views.submission, name='submission'), #for checking score
]