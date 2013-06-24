from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2.views import SingleTableView
from requirements.models import Requirement, RequirementAlternativePath,\
    RequirementStep
from requirements.tables import RequirementTable
from requirements.forms import RequirementPreConditionFormSet,\
    RequirementPostConditionFormSet, RequirementStepFormSet,\
    RequirementAlternativePathForm
from django.http.response import HttpResponseRedirect


class RequirementListView(SingleTableView):
    model = Requirement
    table_class = RequirementTable


class RequirementCreateView(CreateView):
    model = Requirement
    success_url = reverse_lazy("requirements:requirements")
    
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['preconditions_formset'] = RequirementPreConditionFormSet(
            self.request.POST or None,
            instance=self.model()
        )
        context['postconditions_formset'] = RequirementPostConditionFormSet(
            self.request.POST or None,
            instance=self.model()
        )
        context['steps_formset'] = RequirementStepFormSet(
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

        if form.is_valid() and \
            preconditions_formset.is_valid() and \
            postconditions_formset.is_valid() and \
            steps_formset.is_valid():

            self.object = form.save(commit=False)
            self.object.author = self.request.user
            self.object.save()
            preconditions = preconditions_formset.save(commit=False)
            for p in preconditions:
                p.requirement = self.object
                p.save()
            postconditions = postconditions_formset.save(commit=False)
            for p in postconditions:
                p.requirement = self.object
                p.save()
            steps = steps_formset.save(commit=False)
            for s in steps:
                s.requirement = self.object
                s.save()
            
            messages.success(self.request, _(u'Requirement created'))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class RequirementUpdateView(UpdateView):
    model = Requirement
    success_url = reverse_lazy("requirements:requirements")
    
    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context['preconditions_formset'] = RequirementPreConditionFormSet(
            self.request.POST or None,
            instance=self.object
        )
        context['postconditions_formset'] = RequirementPostConditionFormSet(
            self.request.POST or None,
            instance=self.object
        )
        context['steps_formset'] = RequirementStepFormSet(
            self.request.POST or None,
            instance=self.object
        )
        return context

    def form_valid(self, form):
        messages.success(self.request, _(u'Requirement updated'))
        return super(RequirementUpdateView, self).form_valid(form)
    
    def post(self, request, *args, **kwargs):
        result = UpdateView.post(self, request, *args, **kwargs)
        print request.POST
        if 'next' in request.POST:
            return HttpResponseRedirect(request.POST.get('next'))
        else:
            return result


class RequirementDeleteView(DeleteView):
    model = Requirement
    success_url = reverse_lazy("requirements:requirements")


class RequirementAlternativePathStepCreateView(CreateView):
    model = RequirementAlternativePath
    form_class = RequirementAlternativePathForm
    initial = {}

    def get_initial(self):
        return self.initial

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['step'] = self.initial['step']
        return context

    def form_valid(self, form):
        messages.success(self.request, _("Alternative step added"))
        return HttpResponseRedirect(
            reverse_lazy('requirements:requirement_update', 
                            kwargs={'pk': self.initial['step'].requirement.pk})
        )

    def get(self, request, *args, **kwargs):
        self.initial['step'] = RequirementStep.objects.get(pk=kwargs['step_pk']) 
        return CreateView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.initial['step'] = RequirementStep.objects.get(pk=kwargs['step_pk'])
        self.object = self.model()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.step = self.get_context_data()['step']
            self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
