from django.utils.translation import ugettext as _
from requirements.models import Requirement
import django_tables2 as tables


class RequirementTable(tables.Table):
    test_cases = tables.TemplateColumn("{{ record.test_cases.all|length }}",
                                       verbose_name=_("Number of Test Cases"))
    actions = tables.TemplateColumn(template_name='__record_actions.html',
                                    verbose_name=_("Actions"))
    
    class Meta:
        model = Requirement
        attrs = {"class": "table table-bordered table-hover"}