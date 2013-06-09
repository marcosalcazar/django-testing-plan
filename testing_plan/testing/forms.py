from django import forms
from testing.models import TestCasePreCondition, TestCase, \
    TestCasePostCondition, TestCaseStep, TestCaseRevision, \
    TestCaseCorrectiveAction
from django.forms.models import inlineformset_factory


TestCasePreConditionFormSet = \
    inlineformset_factory(TestCase, TestCasePreCondition)


TestCasePostConditionFormSet = \
    inlineformset_factory(TestCase, TestCasePostCondition)


TestCaseStepFormSet = \
    inlineformset_factory(TestCase, TestCaseStep)


TestCaseCorrectiveActionFormSet = \
    inlineformset_factory(TestCase, TestCaseCorrectiveAction)


class TestCaseRevisionForm(forms.ModelForm):
    
    class Meta:
        model = TestCaseRevision
        exclude = ('test_case', 'user', )
