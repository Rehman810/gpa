from django import forms

class RollNumberForm(forms.Form):
    roll_no = forms.CharField(label="Enter Roll Number", max_length=10)