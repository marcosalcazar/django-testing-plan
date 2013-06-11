import django_tables2 as tables
from testing.models import Requirement, TestCase


class RequirementTable(tables.Table):
    actions = tables.TemplateColumn(template_name='__record_actions.html')
    
    class Meta:
        model = Requirement
        attrs = {"class": "table"}


class TestCaseTable(tables.Table):
    actions = tables.TemplateColumn(template_name='__record_actions.html')

    class Meta:
        model = TestCase
        attrs = {"class": "table"}
        exclude = ('objective', 'estimated_execution_time', )