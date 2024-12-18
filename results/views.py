from django.shortcuts import render, redirect
from .models import Result
from .forms import RollNumberForm

# Grade to grade point mapping
GRADE_POINTS = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'F': 0.0,'I':0.0,
}

# Subject credit hours
CREDIT_HOURS = {
    'linear_algebra': 3,
    'oop_theory': 3,
    'oop_practical': 1,
    'pakistan_studies': 2,
    'islamic_studies': 2,
    'digital_logic_theory': 2,
    'digital_logic_practical': 1,
    'communication_skills': 2,
}

def calculate_gpa(result):
    total_points = 0
    total_credits = 0

    # Iterate through each subject, get grade points and calculate GPA
    for subject, credit in CREDIT_HOURS.items():
        grade = getattr(result, subject, None)  # Get the grade for the subject
        if grade and grade in GRADE_POINTS:     # Check if the grade is valid
            total_points += GRADE_POINTS[grade] * credit
            total_credits += credit

    # Avoid division by zero
    if total_credits == 0:
        return 0.0

    # Calculate GPA
    gpa = total_points / total_credits
    return round(gpa, 2)  # Round GPA to 2 decimal places


def roll_number_input(request):
    error_message = None

    if request.method == "POST":
        form = RollNumberForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']
            if Result.objects.filter(roll_no=roll_no).exists():
                return redirect('result_page', roll_no=roll_no)
            else:
                error_message = "No results found for this Roll Number."
    else:
        form = RollNumberForm()

    return render(request, 'input_roll_no.html', {'form': form, 'error_message': error_message})


def result_page(request, roll_no):
    try:
        result = Result.objects.get(roll_no=roll_no)
        gpa = calculate_gpa(result)  # Calculate GPA
    except Result.DoesNotExist:
        result = None
        gpa = None

    return render(request, 'result_page.html', {'result': result, 'roll_no': roll_no, 'gpa': gpa})
