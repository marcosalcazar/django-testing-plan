from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from requirements.views import RequirementListView, RequirementCreateView,\
    RequirementUpdateView, RequirementDeleteView,\
    RequirementAlternativePathStepCreateView


urlpatterns = patterns('testing.views',

    url(r'requirements/$', login_required(RequirementListView.as_view()), name='requirements'),
    url(r'requirement/create/$', login_required(RequirementCreateView.as_view()), name='requirement_create'),
    url(r'requirement/update/(?P<pk>\d+)/$', login_required(RequirementUpdateView.as_view()), name='requirement_update'),
    url(r'requirement/delete/(?P<pk>\d+)/$', login_required(RequirementDeleteView.as_view()), name='requirement_delete'),
    
    url(r'requirement/alternativepath/create/(?P<step_pk>\d+)/$', login_required(RequirementAlternativePathStepCreateView.as_view()), name='alternative_create'),

)
