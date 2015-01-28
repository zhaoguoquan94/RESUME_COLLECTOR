#! coding=utf-8
from django.shortcuts import render
from forms import *
from models import *
# Create your views here.
def handle_resume_upload(request):
    if request.method=="POST":
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            print(str(cd))
            nickname=cd['nickname']
            email=cd["email"]
            reason=cd['reason']
            file=cd['file']
            resume=Resume(nickname=nickname,email=email,reason=reason,file=file)
            resume.save()
            return render(request,"resume_uploader/index.html",{"success":"上传成功!"})
        else:
            return render(request,"resume_uploader/index.html",{"form":form})
    if request.method=="GET":
        return render(request,'resume_uploader/index.html')
