import django_tables2 as tables
from testing.models import TestCase
from django.utils.translation import ugettext_lazy as _


class TestCaseTable(tables.Table):
    author = tables.TemplateColumn(template_name='__record_author_user_display_name.html')
    states = tables.TemplateColumn(
        template_name='testing/__testcase_states.html',
        verbose_name=_("States"))
    actions = tables.TemplateColumn(template_name='__record_actions.html',
                                    sortable=False,
                                    verbose_name=_("Actions"))

    class Meta:
        model = TestCase
        attrs = {"class": "table table-bordered table-hover"}
        sequence = ('id', 'requirement', 'title', 'author', 'test_case_type',
                   'execution_type', 'states')
        exclude = ('objective', 'estimated_execution_time', )