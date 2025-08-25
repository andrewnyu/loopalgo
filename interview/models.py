from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    QUESTION_TYPES = [
        ('coding', 'Coding Question'),
        ('text', 'Text Question'),
    ]
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    type = models.CharField(max_length=6, choices=QUESTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s answer to {self.question.title}"
    
    class Meta:
        unique_together = ['user', 'question']  # One answer per question per user