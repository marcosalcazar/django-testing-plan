from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2.views import SingleTableView
from ho import pisa
from testing.forms import TestCasePreConditionFormSet, \
    TestCasePostConditionFormSet, TestCaseStepFormSet, TestCaseRevisionForm, \
    TestCaseForm
from testing.models import TestCase
from testing.tables import TestCaseTable
import StringIO
import cgi
#from relatorio.templates.opendocument import Template
#from django.conf import settings
#import os
#from django.shortcuts import render_to_response


class TestCaseListView(SingleTableView):
    model = TestCase
    table_class = TestCaseTable


class TestCaseCreateView(CreateView):
    model = TestCase
    form_class = TestCaseForm
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

        if form.is_valid() and \
            preconditions_formset.is_valid() and \
            postconditions_formset.is_valid() and \
            steps_formset.is_valid() and \
            revision_form.is_valid():

            self.object = form.save(commit=False)
            self.object.author = self.request.user
            self.object.save()
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
            messages.success(self.request, _('Test Case created'))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class TestCaseUpdateView(UpdateView):
    model = TestCase
    form_class = TestCaseForm
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
        preconditions_formset.clean()
        if form.is_valid() and \
            preconditions_formset.is_valid() and \
            postconditions_formset.is_valid() and \
            steps_formset.is_valid() and \
            revision_form.is_valid():

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
            messages.success(self.request, _('Test Case updated'))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class TestCaseDeleteView(DeleteView):
    model = TestCase
    success_url = reverse_lazy("testing:testcases")
    template_name = '__confirm_delete.html'


def _generate_pdf(html):
    #Function for generating the PDF file and return it using HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse(_('Error while creating the PDF file: %s' % cgi.escape(html)))
 
 
class TestCasesReportView(View):
    template_name = 'testing/test_cases_report.html'
     
    def get(self, request, *args, **kwargs):
        data = dict(
            test_cases = TestCase.objects.all(),
            pagesize = 'A4',
        )
        html = render_to_string(
            self.template_name, data, context_instance=RequestContext(request))
        return _generate_pdf(html)


# class TestCasesReportView(View):
#     
#     def get(self, request, *args, **kwargs):
#         test_cases = TestCase.objects.all().values()
#         print test_cases
#         templateFilePath = os.path.join(settings.PROJECT_PATH, 'testing', 'reports', 'testcases_skeleton.odt')
#         report = Template(source=open(templateFilePath,'r'),
#                           filepath=templateFilePath)
#         response = HttpResponse(
#             report.generate(test_cases=test_cases).render().getvalue(), 
#             mimetype='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="TestCasesReport.pdf"'
#         return response