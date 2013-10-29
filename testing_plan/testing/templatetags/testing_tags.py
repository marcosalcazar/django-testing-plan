# -*- coding: utf-8 *-*
from django import template
from testing.models import TestCaseState

register = template.Library()


@register.assignment_tag(takes_context=True)
def testcasestates_summary(context):
    test_case = context['record']

    results = []
    for (code, state) in TestCaseState.STATES:
        res = {}
        q_filtered = TestCaseState.objects.filter(test_case=test_case, state=code)
        res["state"] = state
        res["total"] = q_filtered.count()
        if code != "0":
            res["completed"] = q_filtered.filter(completed=True).count()
            res["verified"] = q_filtered.filter(verified=True).count()
        else:
            res["completed"] = " - "
            res["verified"] = " - "
        results.append(res)
    return results
