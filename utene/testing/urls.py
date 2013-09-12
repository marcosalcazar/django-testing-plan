from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from testing.views import TestCaseListView, TestCaseCreateView, \
    TestCaseUpdateView, TestCasesReportView, TestCaseDeleteView,\
    TestCasesReportDoView, TestPlanListView, TestPlanCreateView,\
    TestPlanUpdateView, TestPlanExecutionView, TestPlanExecutionCreateView


urlpatterns = patterns('testing.views',

    url(r'test_cases/$', login_required(TestCaseListView.as_view()), name='testcases'),
    url(r'test_case/create/$', login_required(TestCaseCreateView.as_view()), name='testcase_create'),
    url(r'test_case/update/(?P<pk>\d+)/$', login_required(TestCaseUpdateView.as_view()), name='testcase_update'),
    url(r'test_case/delete/(?P<pk>\d+)/$', login_required(TestCaseDeleteView.as_view()), name='testcase_delete'),
    
    url(r'testing_plan/$', login_required(TestPlanListView.as_view()), name='testingplan'),
    url(r'testing_plan/create/$', login_required(TestPlanCreateView.as_view()), name='testplan_create'),
    url(r'testing_plan/update/(?P<pk>\d+)/$', login_required(TestPlanUpdateView.as_view()), name='testplan_update'),

    url(r'test_cases_report/$', login_required(TestCasesReportView.as_view()), name='testcasesreports'),
    url(r'test_cases_report_do/$', login_required(TestCasesReportDoView.as_view()), name='testcasesreportsdo'),
    
    url(r'testing_plan_execution/(?P<plan_pk>\d+)/$', login_required(TestPlanExecutionView.as_view()), name='testingplanexecution'),
    url(r'testing_plan_executetestcase/(?P<plan_pk>\d+)/(?P<testcase_pk>\d+)/$', login_required(TestPlanExecutionCreateView.as_view()), name='testplan_executetestcase'),

)
