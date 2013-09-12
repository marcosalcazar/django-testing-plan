# -*- coding: utf-8 *-*
from django import template
from testing.models import TestPlanExecution

register = template.Library()


@register.assignment_tag
def testcase_previous_results(plan_pk, testcase_pk):
    return TestPlanExecution.objects.filter(test_plan__pk=plan_pk, test_case__pk=testcase_pk).all()
