from django import forms
from django.forms.models import inlineformset_factory
from testing.models import TestCasePreCondition, TestCase, TestCasePostCondition, \
    TestCaseStep, TestCaseRevision, TestPlanExecution
from utene.forms import ReadOnlyField


TestCasePreConditionFormSet = \
    inlineformset_factory(TestCase, TestCasePreCondition)


TestCasePostConditionFormSet = \
    inlineformset_factory(TestCase, TestCasePostCondition)


TestCaseStepFormSet = \
    inlineformset_factory(TestCase, TestCaseStep)


# TestCaseCorrectiveActionFormSet = \
#     inlineformset_factory(TestCase, TestCaseCorrectiveAction)


class TestCaseRevisionForm(forms.ModelForm):

    class Meta:
        model = TestCaseRevision
        exclude = ('test_case', 'user',)


class TestCaseForm(forms.ModelForm):
    
    class Meta:
        model = TestCase
        exclude = ('author', )


class TestPlanExecutionForm(forms.ModelForm):
    test_plan = ReadOnlyField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )
    test_case = ReadOnlyField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )
    qa_resource = ReadOnlyField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )
    
    class Meta:
        model = TestPlanExecution
        fields = ('test_plan', 'test_case', 'qa_resource', 'result', 'observations', )