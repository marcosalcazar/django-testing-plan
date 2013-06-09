from django.views.generic.list import ListView
from testing.models import Requirement, TestCase
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy
from testing.forms import TestCasePreConditionFormSet,\
    TestCasePostConditionFormSet, TestCaseStepFormSet, TestCaseRevisionForm,\
    TestCaseCorrectiveActionFormSet


class RequirementListView(ListView):
    model = Requirement


class RequirementCreateView(CreateView):
    model = Requirement
    success_url = reverse_lazy("testing:requirements")
    
    def form_valid(self, form):
        messages.success(self.request, _(u'Requirement created'))
        return super(RequirementCreateView, self).form_valid(form)


class RequirementUpdateView(UpdateView):
    model = Requirement
    success_url = reverse_lazy("testing:requirements")
    
    def form_valid(self, form):
        messages.success(self.request, _(u'Requirement updated'))
        return super(RequirementUpdateView, self).form_valid(form)


class TestCaseListView(ListView):
    model = TestCase


class TestCaseCreateView(CreateView):
    model = TestCase
    success_url = reverse_lazy("testing:testcases")
    
    def form_valid(self, form):
        messages.success(self.request, _(u'Test Case created'))
        return super(TestCaseCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['preconditions_formset'] = TestCasePreConditionFormSet(
            self.request.POST or None
        )
        context['postconditions_formset'] = TestCasePostConditionFormSet(
            self.request.POST or None
        )
        context['steps_formset'] = TestCaseStepFormSet(
            self.request.POST or None
        )
        context['revision_form'] = TestCaseRevisionForm(
            self.request.POST or None
        )
        context['correctiveactions_formset'] = TestCaseCorrectiveActionFormSet(
            self.request.POST or None
        )
        return context


class TestCaseUpdateView(UpdateView):
    model = TestCase
    success_url = reverse_lazy("testing:testcases")
    
    def form_valid(self, form):
        messages.success(self.request, _(u'Test Case updated'))
        return super(TestCaseUpdateView, self).form_valid(form)