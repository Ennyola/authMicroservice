from django.db import models
# Create your models here.
class Files(models.Model):
    user = models.CharField(max_length=50)
    file = models.FileField(upload_to='./uploaded_files')