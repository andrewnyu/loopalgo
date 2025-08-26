from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Choose a unique username for your account'
    )
    email = forms.EmailField(
        required=True,
        help_text='Your email address for account recovery'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=255,
        required=True,
        help_text='Your full name as it appears on official documents'
    )
    
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        help_text='Your date of birth'
    )
    
    school = forms.CharField(
        max_length=255,
        required=False,
        help_text='Your current school or institution (optional)'
    )
    
    grade_level = forms.CharField(
        max_length=50,
        required=False,
        help_text='Your current grade level or year (optional)'
    )
    
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False,
        help_text='Your mailing address (optional)'
    )
    
    competitions = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text='List any math or coding competitions you\'ve participated in (optional)'
    )
    
    interests = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text='Your interests in mathematics, programming, or computer science (optional)'
    )
    
    class Meta:
        model = UserProfile
        fields = ('full_name', 'birthday', 'school', 'grade_level', 
                 'address', 'competitions', 'interests')