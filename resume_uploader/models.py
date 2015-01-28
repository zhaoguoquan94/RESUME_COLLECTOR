from django.db import models
import datetime
# Create your models here.
def handle_file_upload(instance,filename):
    return datetime.datetime.now().strftime("%Y%m%d%X")+"_"+instance.nickname+"_"+filename
class Resume(models.Model):

    nickname=models.CharField(max_length=128)
    email=models.EmailField(max_length=128)
    reason=models.TextField(max_length=1024)
    file=models.FileField(upload_to=handle_file_upload)