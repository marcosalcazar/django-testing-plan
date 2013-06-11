from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy


class Requirement(models.Model):
    
    REQUIREMENT_TYPES = (
        ('FC', _('Functional')),
        ('US', _('Usability')),
        ('RE', _('Reliability')),
        ('PE', _('Performance')),
        ('SU', _('Supportability')),
        ('IM', _('(+) Implementation')),
        ('IN', _('(+) Interfaces (Not GUI)')),
        ('OP', _('(+) Operations')),
        ('EM', _('(+) Packaging')),
        ('LE', _('(+) Legals')),
    )

    type = models.CharField(verbose_name=_('Requirement Type'), 
                            max_length=2,
                            choices=REQUIREMENT_TYPES)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    def __unicode__(self):
        return u"[%s] %s" % (self.get_type_display(), self.name)
    
    def get_absolute_url(self):
        return reverse_lazy('testing:requirement_update', 
                            kwargs={'pk': self.pk})
        
    def get_absolute_delete_url(self):
        return reverse_lazy('testing:requirement_delete', 
                            kwargs={'pk': self.pk})


class TestCase(models.Model):
    
    EXECUTION_TYPES = (
        ('M', _('Manual')),
        ('A', _('Automated'))
    )
    
    TEST_CASE_TYPES = (
        ('U', _('Unit')),
        ('I', _('Integration')),
        ('S', _('Security')),
        ('G', _('System')),
        ('A', _('Acceptance')),
        ('C', _('Load'))
    )
    
    title = models.CharField(_('Title'), max_length=255)
    author = models.ForeignKey(User, verbose_name=_('Author'))
    objective = models.TextField(_('Objective'))
    test_case_type = models.CharField(_('Type'),
                                      max_length=1, 
                                      choices=TEST_CASE_TYPES)
    requirement = models.ForeignKey(Requirement, 
                                    verbose_name=_('Requirement'),
                                    related_name='test_cases')
    execution_type = models.CharField(verbose_name=_('Execution Type'),
                                      max_length=2,
                                      choices=EXECUTION_TYPES)
    estimated_execution_time = \
        models.PositiveIntegerField(_('Estimated Execution Time'))
    
    def __unicode__(self):
        return "%s - %s" % (self.id, self.title)
    
    def get_absolute_url(self):
        return reverse_lazy('testing:testcase_update', 
                            kwargs={'pk': self.pk})
    
    def get_absolute_delete_url(self):
        return reverse_lazy('testing:testcase_delete', 
                            kwargs={'pk': self.pk})


class TestCasePreCondition(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='preconditions')
    description = models.CharField(verbose_name=_('Description'), 
                                   max_length=255)
    
    def __unicode__(self):
        return self.description


class TestCasePostCondition(models.Model):

    test_case = models.ForeignKey(TestCase, related_name='postconditions')
    description = models.CharField(verbose_name=_('Description'), 
                                   max_length=255)
    
    def __unicode__(self):
        return self.description


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
    description = models.CharField(verbose_name=_('Description'), 
                                   max_length=255)
    
    def __unicode__(self):
        return self.description
