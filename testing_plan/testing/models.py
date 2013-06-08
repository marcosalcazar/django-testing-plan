from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy


class Requirement(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('testing:requirement_update', 
                            kwargs={'pk': self.pk})


class TestCase(models.Model):
    
    EXECUTION_TYPES = (
        ('M', _('Manual')),
        ('A', _('Automated'))
    )
    
    title = models.CharField(_('Title'), max_length=255)
    author = models.ForeignKey(User, verbose_name=_('Author'))
    objective = models.TextField(_('Objective'))
    requeriment = models.ForeignKey(Requirement, verbose_name=_('Requirement'))
    execution_type = models.CharField(verbose_name=_('Execution Type'),
                                      max_length=2,
                                      choices=EXECUTION_TYPES)
    estimated_execution_time = \
        models.PositiveIntegerField(_('Estimated Execution Time'))
    
    def __unicode__(self):
        return self.id
    
    def get_absolute_url(self):
        return reverse_lazy('testing:testcase_update', 
                            kwargs={'pk': self.pk})


class TestCasePreCondition(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='preconditions')
    description = models.TextField(verbose_name=_('Description'))


class TestCasePostCondition(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='postconditions')
    description = models.TextField(verbose_name=_('Description'))


class TestCaseRevision(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='revisions')
    user = models.ForeignKey(User, verbose_name=_('User'))
    description = models.CharField(_('Description'), max_length=255)
    date = models.DateTimeField(_('Date'), auto_now_add=True)


class TestCaseStep(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='steps')
    step_number = models.PositiveSmallIntegerField(_('Step number'))
    step_action = models.TextField(_('Step action'))
    step_expected_result = models.TextField(_('Expected Result'))


class TestCaseCorrectiveAction(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='corrective_actions')
    description = models.TextField(_('Description'))
