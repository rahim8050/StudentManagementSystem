from django import forms

from student.models import Student

GENDER_CHOICES = {"Male": "Male", "Female": "Female"}

class StudentForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model = Student
        fields = ['FirstName', 'LastName', 'Email', 'Age', 'Weight','Gender','AdmissionNumber','Semester','Address']
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Age': forms.DateInput(attrs={'type':'number',}),
            'Weight': forms.TextInput(attrs={'type':'number','min':'0','max':'100'}),
            'AdmissionNumber': forms.TextInput(attrs={ 'type':'number','class':'form-control'}),
            'Gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'Semester': forms.TextInput(attrs={'class': 'form-control'}),
        }