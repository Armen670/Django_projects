from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserBioForm(forms.Form):
    name = forms.CharField(label="Name:")
    age = forms.IntegerField(label="Age:",min_value=0,max_value=125)
    bio = forms.CharField(label="Biography:",widget=forms.Textarea)

def validate_file_name(file: InMemoryUploadedFile) -> None:
    if file.name and 'virus' in file.name:
        raise ValidationError("File name must not contain word 'virus'")

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_name])