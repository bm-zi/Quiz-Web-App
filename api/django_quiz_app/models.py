from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum


class Quiz(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = RichTextField(blank=True, null=True)
    total_points = models.IntegerField(default=0, editable=False)  # Automatically calculated

    def update_total_points(self):
        # Calculate total points by summing the points from related questions
        total = self.questions.aggregate(total=Sum('points'))['total'] or 0
        self.total_points = total
        self.save()

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    description = RichTextField(blank=True, null=True)
    options = models.JSONField()  # Store options as a JSON object
    correct_option = models.IntegerField()  # Store the index of the correct option
    points = models.IntegerField(default=0)  # Points awarded for this question

    def __str__(self):
        return self.question_text


# Signals to update total points in Quiz when a Question is created, updated, or deleted
@receiver(post_save, sender=Question)
def update_quiz_total_points_on_save(sender, instance, **kwargs):
    instance.quiz.update_total_points()

@receiver(post_delete, sender=Question)
def update_quiz_total_points_on_delete(sender, instance, **kwargs):
    instance.quiz.update_total_points()
