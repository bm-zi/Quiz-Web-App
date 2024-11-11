import json
from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework import viewsets, generics
from rest_framework.exceptions import NotFound
from django_quiz_app.models import Quiz, Question
from django_quiz_app.serializers import QuestionSerializer, QuizSerializer, QuizNamesSerializer
from django_quiz_app.forms import QuizJsonUploadForm, QuestionUploadForm

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse


class QuizNamesViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizNamesSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def upload_quiz_json(request):
    if request.method == 'POST':
        form = QuizJsonUploadForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.cleaned_data['quiz']
            json_file = request.FILES['json_file']

            try:
                data = json.load(json_file)

                # Validate the JSON structure
                if 'questions' not in data or not isinstance(data['questions'], list):
                    messages.error(request, "Invalid JSON format: 'questions' key must be present and should be a list.")
                    return redirect('upload_quiz_json')

                questions = data['questions']

                for i, question_data in enumerate(questions):
                    if not isinstance(question_data, dict):
                        messages.error(request, f"Invalid format for question at index {i + 1}. Each question should be an object.")
                        return redirect('upload_quiz_json')

                    required_keys = ['question_text', 'options', 'correct_option']
                    for key in required_keys:
                        if key not in question_data:
                            messages.error(request, f"Missing required field '{key}' for question at index {i + 1}.")
                            return redirect('upload_quiz_json')

                    options = question_data['options']
                    if not isinstance(options, list) or len(options) < 2:
                        messages.error(request, f"'options' must be a list with at least two elements for question at index {i + 1}.")
                        return redirect('upload_quiz_json')

                    correct_option = question_data['correct_option']
                    # Adjust validation to allow 0-based indexing
                    if not isinstance(correct_option, int) or correct_option < 0 or correct_option >= len(options):
                        messages.error(request, f"Invalid 'correct_option' for question at index {i + 1}. It should be an integer between 0 and {len(options) - 1}.")
                        return redirect('upload_quiz_json')

                    question_text = question_data['question_text']
                    points = question_data.get('points', 0)

                    Question.objects.create(
                        quiz=quiz,
                        question_text=question_text,
                        options=options,
                        correct_option=correct_option,
                        points=points
                    )

                messages.success(request, f"Successfully uploaded and assigned {len(questions)} questions to {quiz.name}.")
                return redirect('upload_quiz_json')

            except json.JSONDecodeError:
                messages.error(request, "Invalid JSON file format.")
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")

    else:
        form = QuizJsonUploadForm()

    return render(request, 'django_quiz_app/upload_quiz_json.html', {'form': form})


class QuizQuestionsByNameView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_name = self.kwargs['quiz_name']
        try:
            quiz = Quiz.objects.get(name=quiz_name)
        except Quiz.DoesNotExist:
            raise NotFound(f"Quiz with name '{quiz_name}' does not exist.")
        
        return Question.objects.filter(quiz=quiz)



def upload_questions(request):
    if request.method == 'POST':
        form = QuestionUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            try:
                # Load JSON data from the file
                data = json.load(file)

                # Check if `data` is a list
                if not isinstance(data, list):
                    messages.error(request, "The JSON file must contain a list of questions.")
                    return redirect('upload_questions')

                # Iterate through each item in data, which should be a dictionary
                for item in data:
                    if not isinstance(item, dict):
                        messages.error(request, "Each question must be a JSON object.")
                        return redirect('upload_questions')

                    quiz_name = item.get('quiz')
                    question_text = item.get('question_text')
                    description = item.get('description', "")
                    options = item.get('options', [])
                    correct_option = item.get('correct_option', 0)
                    points = item.get('points', 0)

                    # Ensure quiz exists or create it
                    quiz, created = Quiz.objects.get_or_create(name=quiz_name)

                    # Create the question
                    Question.objects.create(
                        quiz=quiz,
                        question_text=question_text,
                        description=description,
                        options=options,
                        correct_option=correct_option,
                        points=points
                    )

                messages.success(request, "Questions uploaded successfully!")
                return redirect('upload_questions')
            except json.JSONDecodeError:
                messages.error(request, "Invalid JSON file format.")
            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {e}")
    else:
        form = QuestionUploadForm()

    return render(request, 'django_quiz_app/upload_questions.html', {'form': form})


def download_json(request):
    """
    download the questions as a JSON file
    """
    # Get data from the model
    data = Question.objects.all().filter(quiz__name="python-01")

    # Serialize data to JSON format
    data_json = serialize('json', data)

    # Create the HttpResponse object with JSON headers
    response = HttpResponse(data_json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="question_data.json"'

    return response


def get_json_data(request):
    """
    JSON data directly as an API response without a file download
    """
    # Get data from the model and convert it to a list of dictionaries
    data = list(Question.objects.values())

    # Return JSON data as a JsonResponse
    return JsonResponse(data, safe=False)