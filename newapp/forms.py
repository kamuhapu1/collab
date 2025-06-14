from django import forms
from .models import TableBooking, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'phone', 'day', 'hour', 'persons']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Оставьте ваш комментарий...'
            }),
        }