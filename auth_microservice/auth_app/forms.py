from .models import Files
from django.forms import ModelForm

class UploadFileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['user', 'file']

