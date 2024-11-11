from rest_framework import serializers
from .models import Quiz, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'description', 'options', 'correct_option', 'points']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    total_points = serializers.IntegerField(read_only=True)  # Read-only, calculated automatically

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'total_points', 'questions']


class QuizNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['name']
