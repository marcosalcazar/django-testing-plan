from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.utils.translation import ugettext as _
from testing.models import TestCasePreCondition, TestCase, TestCasePostCondition, \
    TestCaseStep, TestCaseRevision, TestCaseCorrectiveAction


# class RequireOneFormSet(BaseInlineFormSet):
#     """Require at least one form in the formset to be completed."""
# 
#     def clean(self):
#         print "clean"
#         """Check that at least one form has been completed."""
#         super(RequireOneFormSet, self).clean()
#         for error in self.errors:
#             if error:
#                 return
#         completed = 0
#         for cleaned_data in self.cleaned_data:
#             # form has data and we aren't deleting it.
#             if cleaned_data and not cleaned_data.get('DELETE', False):
#                 completed += 1
# 
#         if completed < 1:
#             raise forms.ValidationError("At least one %s is required." %
#                 self.model._meta.object_name.lower())


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
        exclude = ('test_case', 'user',)
