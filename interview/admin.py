from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('title', 'text')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'submitted_at')
    list_filter = ('submitted_at', 'question')
    search_fields = ('user__username', 'question__title', 'answer_text')

# Register the models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)