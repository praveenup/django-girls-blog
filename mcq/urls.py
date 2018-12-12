from django.urls import path

from . import views
app_name = 'mcq'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/mark/', views.mark, name='mark'),
    path('submission/', views.submission, name='submission'),
]