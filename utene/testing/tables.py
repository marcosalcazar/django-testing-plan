import django_tables2 as tables
from testing.models import TestCase, TestPlan
from django.utils.translation import ugettext_lazy as _


DEFAULT_TABLE_ATTRS = {"class": "table table-bordered table-hover"}


class TestCaseTable(tables.Table):
    author = tables.TemplateColumn(template_name='__record_author_user_display_name.html')
    actions = tables.TemplateColumn(template_name='__record_actions.html',
                                    sortable=False,
                                    verbose_name=_("Actions"))
    
    class Meta:
        model = TestCase
        attrs = DEFAULT_TABLE_ATTRS
        sequence = ('id', 'requirement', 'title', 'author', 'test_case_type',
                   'execution_type')
        exclude = ('objective', 'estimated_execution_time', )


class TestPlanTable(tables.Table):
    actions = tables.TemplateColumn(template_name='testing/__test_plan_actions.html',
                                    sortable=False,
                                    verbose_name=_("Actions"))
    
    class Meta:
        model = TestPlan
        attrs = DEFAULT_TABLE_ATTRS
        sequence = ('id', 'name', 'start_date', 'end_date', 'actions')


class TestCasesForPlanExecutionTable(tables.Table):
    previous_results = tables.TemplateColumn(template_name='testing/__test_plan_execution_previous_results.html',
                                             sortable=False,
                                             verbose_name=_("Previous Results"))
    actions = tables.TemplateColumn(template_name='testing/__test_plan_execution_actions.html',
                                    sortable=False,
                                    verbose_name=_("Actions"))
    
    class Meta:
        model = TestCase
        attrs = DEFAULT_TABLE_ATTRS
        sequence = ('id', 'requirement', 'title', 'test_case_type', 'execution_type', 'previous_results', 'actions')
        exclude = ('objective', 'estimated_execution_time', 'author', )
        