#! coding=utf-8
from django import forms
class ResumeForm(forms.Form):
    nickname=forms.CharField(max_length=128)
    email=forms.EmailField(max_length=128)
    reason=forms.CharField(max_length=1024)
    file=forms.FileField()
    def clean_file(self):
        from django.template.defaultfilters import filesizeformat
        from django.utils.translation import ugettext_lazy as _
        content = self.cleaned_data['file']
        content_type = content.content_type.split('/')[1]
        if content_type in ['pdf','msword','vnd.openxmlformats-officedocument.wordprocessingml.document']:
            if content._size > 20971520:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(20971520), filesizeformat(content._size)))
        else:
            raise forms.ValidationError(_('文件格式不支持,请上传PDF,doc,docx格式'))
        return content

