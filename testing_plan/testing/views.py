from django.views.generic.list import ListView
from testing.models import Requirement, TestCase
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy
from testing.forms import TestCasePreConditionFormSet,\
    TestCasePostConditionFormSet, TestCaseStepFormSet, TestCaseRevisionForm,\
    TestCaseCorrectiveActionFormSet
from django.http.response import HttpResponse, HttpResponseRedirect


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
    
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['preconditions_formset'] = TestCasePreConditionFormSet(
            self.request.POST or None,
            instance=self.model()
        )
        context['postconditions_formset'] = TestCasePostConditionFormSet(
            self.request.POST or None,
            instance=self.model()
        )
        context['steps_formset'] = TestCaseStepFormSet(
            self.request.POST or None,
            instance=self.model()
        )
        context['revision_form'] = TestCaseRevisionForm(
            self.request.POST or None
        )
        context['correctiveactions_formset'] = TestCaseCorrectiveActionFormSet(
            self.request.POST or None,
            instance=self.model()
        )
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.model()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data()
        preconditions_formset = context['preconditions_formset']
        postconditions_formset = context['postconditions_formset']
        steps_formset = context['steps_formset']
        revision_form = context['revision_form']
        correctiveactions_formset = context['correctiveactions_formset']
        preconditions_formset.clean()
        if form.is_valid() and \
            preconditions_formset.is_valid() and \
            postconditions_formset.is_valid() and \
            steps_formset.is_valid() and \
            revision_form.is_valid() and \
            correctiveactions_formset.is_valid():

            self.object = form.save()
            preconditions = preconditions_formset.save(commit=False)
            for p in preconditions:
                p.test_case = self.object
                p.save()
            postconditions = postconditions_formset.save(commit=False)
            for p in postconditions:
                p.test_case = self.object
                p.save()
            steps = steps_formset.save(commit=False)
            for s in steps:
                s.test_case = self.object
                s.save()
            revision = revision_form.save(commit=False)
            revision.test_case = self.object
            revision.user = self.request.user
            revision.save()
            correctiveactions = correctiveactions_formset.save(commit=False)
            for c in correctiveactions:
                c.test_case = self.object
                c.save()
            messages.success(self.request, _('Test Case created'))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)
            


class TestCaseUpdateView(UpdateView):
    model = TestCase
    success_url = reverse_lazy("testing:testcases")
    
    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context['preconditions_formset'] = TestCasePreConditionFormSet(
            self.request.POST or None,
            instance=self.object
        )
        context['postconditions_formset'] = TestCasePostConditionFormSet(
            self.request.POST or None,
            instance=self.object
        )
        context['steps_formset'] = TestCaseStepFormSet(
            self.request.POST or None,
            instance=self.object
        )
        context['revision_form'] = TestCaseRevisionForm(
            self.request.POST or None
        )
        context['correctiveactions_formset'] = TestCaseCorrectiveActionFormSet(
            self.request.POST or None,
            instance=self.object
        )
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data()
        preconditions_formset = context['preconditions_formset']
        postconditions_formset = context['postconditions_formset']
        steps_formset = context['steps_formset']
        revision_form = context['revision_form']
        correctiveactions_formset = context['correctiveactions_formset']
        preconditions_formset.clean()
        if form.is_valid() and \
            preconditions_formset.is_valid() and \
            postconditions_formset.is_valid() and \
            steps_formset.is_valid() and \
            revision_form.is_valid() and \
            correctiveactions_formset.is_valid():

            self.object = form.save()
            preconditions = preconditions_formset.save(commit=False)
            for p in preconditions:
                p.test_case = self.object
                p.save()
            postconditions = postconditions_formset.save(commit=False)
            for p in postconditions:
                p.test_case = self.object
                p.save()
            steps = steps_formset.save(commit=False)
            for s in steps:
                s.test_case = self.object
                s.save()
            revision = revision_form.save(commit=False)
            revision.test_case = self.object
            revision.user = self.request.user
            revision.save()
            correctiveactions = correctiveactions_formset.save(commit=False)
            for c in correctiveactions:
                c.test_case = self.object
                c.save()
            messages.success(self.request, _('Test Case updated'))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)