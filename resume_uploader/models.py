#! coding=utf-8
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
    def __unicode__(self):
        return u"姓名:"+self.nickname+u"\nemail:"+self.email+u"\n推荐理由:"+self.reason+u"\n文件名:"+self.file.name