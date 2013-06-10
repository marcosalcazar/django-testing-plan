from django.conf.urls import patterns, include, url

#from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

#admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', login_required(TemplateView.as_view(template_name='base.html')), name='home'),
    url(r'^testing/', include('testing.urls', namespace='testing')),
    
    #url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}, name='logout')

)
