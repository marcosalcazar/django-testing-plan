import django_tables2 as tables
from testing.models import Requirement, TestCase
from django.utils.translation import ugettext_lazy as _


class RequirementTable(tables.Table):
    test_cases = tables.TemplateColumn("{{ record.test_cases.all|length }}",
                                       verbose_name=_("Number of Test Cases"))
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