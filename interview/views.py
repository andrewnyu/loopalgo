from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Question, Answer
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.db import transaction

def register(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            try:
                with transaction.atomic():
                    # Create the user first
                    user = user_form.save()
                    
                    # Create the profile and link it to the user
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.save()
                    
                    messages.success(request, 'Registration successful! Please log in.')
                    return redirect('question_list')
            except Exception as e:
                messages.error(request, f'An error occurred during registration. Please try again.')
                user_form = ExtendedUserCreationForm()
                profile_form = UserProfileForm()
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
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