import django_tables2 as tables
from testing.models import TestCase


class TestCaseTable(tables.Table):
    author = tables.TemplateColumn(template_name='__record_author_user_display_name.html')
    actions = tables.TemplateColumn(template_name='__record_actions.html')

    class Meta:
        model = TestCase
        attrs = {"class": "table table-bordered table-hover"}
        exclude = ('objective', 'estimated_execution_time', )