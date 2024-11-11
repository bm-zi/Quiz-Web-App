from django import forms
from .models import Quiz

class QuizJsonUploadForm(forms.Form):
    quiz = forms.ModelChoiceField(queryset=Quiz.objects.all(), required=True)  # Dropdown to select quiz
    json_file = forms.FileField(required=True, help_text="Upload a JSON file containing quiz data")

class QuestionUploadForm(forms.Form):
    file = forms.FileField(label="Upload JSON file")