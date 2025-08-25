from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Question, Answer
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    # Get the questions that the user has already answered
    answered_questions = Answer.objects.filter(user=request.user).values_list('question_id', flat=True)
    return render(request, 'interview/question_list.html', {
        'questions': questions,
        'answered_questions': answered_questions
    })

@login_required
def submit_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    
    if request.method == 'POST':
        answer_text = request.POST.get('answer_text')
        if answer_text:
            Answer.objects.update_or_create(
                user=request.user,
                question=question,
                defaults={'answer_text': answer_text}
            )
            messages.success(request, 'Answer submitted successfully!')
            return redirect('question_list')
        else:
            messages.error(request, 'Answer cannot be empty!')
    
    return render(request, 'interview/submit_answer.html', {'question': question})