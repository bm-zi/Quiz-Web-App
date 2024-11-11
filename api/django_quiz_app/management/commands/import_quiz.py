import json
from django.core.management.base import BaseCommand
from django_quiz_app.models import Quiz  # Replace 'your_app' with the actual app name

class Command(BaseCommand):
    help = 'Load quiz data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path of the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                questions = data.get('questions', [])  # Access the list of questions
                
                for item in questions:
                    # Create Quiz instance from each item
                    Quiz.objects.create(
                        question=item['question'],
                        options=item['options'],  # Assumes options is a list
                        description=item.get('description', ''),  # Default to empty string if not present
                        correct_option=item['correct_option'],  # Required field
                        points=item.get('points', 0)  # Default to 0 if not present
                    )
                self.stdout.write(self.style.SUCCESS('Successfully uploaded JSON data into the database'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON. Please check your file format.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'The file {file_path} was not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
