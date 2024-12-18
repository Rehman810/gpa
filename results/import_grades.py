import os
import django

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  # Replace 'your_project_name' with your project name
django.setup()

from results.models import Result  # Replace 'your_app_name' with your app name

# Data as a list of dictionaries
data = [
    {'roll_no': '23-AI-01', 'linear_algebra': 'B+', 'oop_theory': 'A-', 'oop_practical': 'A', 
     'pakistan_studies': 'A-', 'islamic_studies': 'A-', 'digital_logic_theory': 'A', 
     'digital_logic_practical': 'A', 'communication_skills': 'B+'},
     
    {'roll_no': '23-AI-02', 'linear_algebra': 'B+', 'oop_theory': 'A', 'oop_practical': 'A', 
     'pakistan_studies': 'B+', 'islamic_studies': 'A-', 'digital_logic_theory': 'A', 
     'digital_logic_practical': 'A', 'communication_skills': 'B'},

    {'roll_no': '23-AI-03', 'linear_algebra': 'B-', 'oop_theory': 'B+', 'oop_practical': 'B+', 
     'pakistan_studies': 'B+', 'islamic_studies': 'A-', 'digital_logic_theory': 'B+', 
     'digital_logic_practical': 'B+', 'communication_skills': 'A'},

    # Add all other rows here in the same format
]

def insert_results():
    for row in data:
        Result.objects.update_or_create(
            roll_no=row['roll_no'],  # Primary key or unique field
            defaults=row             # Update or insert the rest of the data
        )
    print("Data has been successfully added to the database!")

if __name__ == "__main__":
    insert_results()
