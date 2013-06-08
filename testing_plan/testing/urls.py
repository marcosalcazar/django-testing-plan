from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from testing.views import RequirementListView, RequirementCreateView,\
    RequirementUpdateView, TestCaseListView, TestCaseCreateView,\
    TestCaseUpdateView


urlpatterns = patterns('testing.views',

    url(r'requirements/$', login_required(RequirementListView.as_view()), name='requirements'),
    url(r'requirement/create/$', login_required(RequirementCreateView.as_view()), name='requirement_create'),
    url(r'requirement/update/(?P<pk>\d+)/$', login_required(RequirementUpdateView.as_view()), name='requirement_update'),
    
    url(r'test_cases/$', login_required(TestCaseListView.as_view()), name='testcases'),
    url(r'test_case/create/$', login_required(TestCaseCreateView.as_view()), name='testcase_create'),
    url(r'test_case/update/(?P<pk>\d+)/$', login_required(TestCaseUpdateView.as_view()), name='testcase_update'),
    
    
)
