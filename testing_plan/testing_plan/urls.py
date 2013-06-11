from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', login_required(RedirectView.as_view(url='/testing/requirements/')), name='home'),
    url(r'^testing/', include('testing.urls', namespace='testing')),
    url(r'^user/', include('user.urls', namespace='user')),
    
    #url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}, name='logout')

)
