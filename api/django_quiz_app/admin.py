from django.contrib import admin
from .models import Quiz, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Allows adding one extra blank question

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_points')  # Display the total points in the list view
    inlines = [QuestionInline]  # Allows questions to be managed inline within a quiz

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'points')  # Display question and points in the list


