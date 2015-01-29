from django.conf.urls import patterns, include, url
from resume_uploader.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RESUME.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',handle_resume_upload),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload_file/(.*)',handle_resume_download)
)
