from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_quiz_app.views import (
    upload_quiz_json, 
    QuizViewSet, 
    QuestionViewSet, 
    QuizQuestionsByNameView, 
    QuizNamesViewSet, 
    upload_questions,
    download_json,
    get_json_data,
    )

from django.conf import settings
from django.conf.urls.static import static


# DRF Router for API endpoints
router = DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'quiznames', QuizNamesViewSet, basename='quiz-names')
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line to enable the Django admin
    path('api/', include(router.urls)),  # The API routes will be prefixed with 'api/'
    path('upload_quiz_json/', upload_quiz_json, name='upload_quiz_json'),
    path('api/quiz/<str:quiz_name>/questions/', QuizQuestionsByNameView.as_view(), name='quiz-questions'),
    path('upload_questions/', upload_questions, name='upload_questions'),
    path('download-json/', download_json, name='download_json'),
    path('get-json-data/', get_json_data, name='get_json_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
