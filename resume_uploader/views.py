#! coding=utf-8
from django.shortcuts import render,redirect
from forms import *
from models import *
from django.http import HttpResponse
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
def handle_resume_download(request,url):
    if not request.user.is_authenticated():
        return redirect("/admin")
    resumes=Resume.objects.all()
    selected_resume=None
    for resume in resumes:
        if resume.file.name==url:
            selected_resume=resume
            break
    if selected_resume  is None:
        return HttpResponse("No match")
    data=selected_resume.file.read()
    response=HttpResponse(data,content_type="application/force-download")
    response['Content-Disposition'] = 'attachment; filename=%s' % selected_resume.file.name.encode("utf-8")
    return response
def handle_resume_search(request):
    if request.method=="POST":
        emailform=EmailForm(request.POST)
        if emailform.is_valid():
            resumes=Resume.objects.filter(email=emailform.cleaned_data['email'])
            responsestr=""
            for r in resumes:
                responsestr+=unicode(r)+u"<br>\n\n"
            return HttpResponse(responsestr)

