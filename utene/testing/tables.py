import django_tables2 as tables
from testing.models import TestCase, TestPlan
from django.utils.translation import ugettext_lazy as _


class TestCaseTable(tables.Table):
    author = tables.TemplateColumn(template_name='__record_author_user_display_name.html')
    actions = tables.TemplateColumn(template_name='__record_actions.html',
                                    sortable=False,
                                    verbose_name=_("Actions"))

    class Meta:
        model = TestCase
        attrs = {"class": "table table-bordered table-hover"}
        sequence = ('id', 'requirement', 'title', 'author', 'test_case_type',
                   'execution_type')
        exclude = ('objective', 'estimated_execution_time', )


class TestPlanTable(tables.Table):
    
    class Meta:
        model = TestPlan
        attrs = {"class": "table table-bordered table-hover"}