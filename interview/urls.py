from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('register/', views.register, name='register'),
    path('question/<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
]
