from django.forms.models import inlineformset_factory
from requirements.models import Requirement, RequirementPreCondition,\
    RequirementPostCondition, RequirementStep, RequirementAlternativePathStep,\
    RequirementAlternativePath
from django import forms


RequirementPreConditionFormSet = \
    inlineformset_factory(Requirement, RequirementPreCondition)


RequirementPostConditionFormSet = \
    inlineformset_factory(Requirement, RequirementPostCondition)


RequirementStepFormSet = \
    inlineformset_factory(Requirement, RequirementStep)


RequirementAlternativePathStepFormSet = \
    inlineformset_factory(RequirementAlternativePath, 
                          RequirementAlternativePathStep)
    

class RequirementAlternativePathForm(forms.ModelForm):
    
    class Meta:
        model = RequirementAlternativePath
        exclude = ('step', )