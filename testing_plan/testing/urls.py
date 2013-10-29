from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from testing.views import TestCaseListView, TestCaseCreateView, \
    TestCaseUpdateView, TestCasesReportView, TestCaseDeleteView,\
    TestCaseDetailView, TestCaseStateDetailView, TestCaseStateCreateView,\
    TestCaseStateDeleteView


urlpatterns = patterns('testing.views',

    url(r'test_cases/$', login_required(TestCaseListView.as_view()), name='testcases'),
    url(r'test_case/create/$', login_required(TestCaseCreateView.as_view()), name='testcase_create'),
    url(r'test_case/view/(?P<pk>\d+)/$', login_required(TestCaseDetailView.as_view()), name='testcase_view'),
    url(r'test_case/update/(?P<pk>\d+)/$', login_required(TestCaseUpdateView.as_view()), name='testcase_update'),
    url(r'test_case/delete/(?P<pk>\d+)/$', login_required(TestCaseDeleteView.as_view()), name='testcase_delete'),

    url(r'test_cases_report/$', login_required(TestCasesReportView.as_view()), name='testcasesreports'),
    
    url(r'test_case_state/create/(?P<testcase_pk>\d+)/$', login_required(TestCaseStateCreateView.as_view()), name='testcasestate_create'),
    url(r'test_case_state/view/(?P<pk>\d+)/$', login_required(TestCaseStateDetailView.as_view()), name='testcasestate_detail'),
    url(r'test_case_state/delete/(?P<pk>\d+)/$', login_required(TestCaseStateDeleteView.as_view()), name='testcasestate_delete'),

)
