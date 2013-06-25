from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2.views import SingleTableView
from requirements.models import Requirement
from requirements.tables import RequirementTable


class RequirementListView(SingleTableView):
    model = Requirement
    table_class = RequirementTable


class RequirementCreateView(CreateView):
    model = Requirement
    success_url = reverse_lazy("requirements:requirements")
    
    def form_valid(self, form):
        messages.success(self.request, _(u'Requirement created'))
        return super(RequirementCreateView, self).form_valid(form)


class RequirementUpdateView(UpdateView):
    model = Requirement
    success_url = reverse_lazy("requirements:requirements")
    
    def form_valid(self, form):
        messages.success(self.request, _(u'Requirement updated'))
        return super(RequirementUpdateView, self).form_valid(form)


class RequirementDeleteView(DeleteView):
    model = Requirement
    success_url = reverse_lazy("requirements:requirements")