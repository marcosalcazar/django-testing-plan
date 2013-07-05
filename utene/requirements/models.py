from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


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
    objective = models.TextField(_('Objective'), default="" )
    responsible = models.ForeignKey(User, verbose_name=_("Responsible"), 
                                    null=True)

    def __unicode__(self):
        return u"[%s] %s" % (self.get_type_display(), self.name)
    
    def get_absolute_url(self):
        return reverse_lazy('requirements:requirement_update', 
                            kwargs={'pk': self.pk})
        
    def get_absolute_delete_url(self):
        return reverse_lazy('requirements:requirement_delete', 
                            kwargs={'pk': self.pk})


class RequirementPreCondition(models.Model):

    requirement = models.ForeignKey(Requirement, related_name='preconditions')
    description = models.CharField(verbose_name=_('Description'), 
                                   max_length=255)
    
    def __unicode__(self):
        return self.description


class RequirementPostCondition(models.Model):

    requirement = models.ForeignKey(Requirement, related_name='postconditions')
    description = models.CharField(verbose_name=_('Description'), 
                                   max_length=255)
    
    def __unicode__(self):
        return self.description


class RequirementRevision(models.Model):

    requirement = models.ForeignKey(Requirement, related_name='revisions')
    user = models.ForeignKey(User, verbose_name=_('User'))
    description = models.CharField(_('Description'), max_length=255)
    date = models.DateTimeField(_('Date'), auto_now_add=True)


class RequirementStep(models.Model):

    requirement = models.ForeignKey(Requirement, related_name='steps')
    step_number = models.PositiveSmallIntegerField(_('Step number'))
    description = models.TextField(_('Description'))
    
    def __unicode__(self):
        return "%s - %s..." % (self.step_number, self.description[0:80])


class RequirementAlternativePath(models.Model):
    step = models.ForeignKey(RequirementStep, related_name=_('alternatives'))
    description = models.TextField(_('Description'))
    
    def __unicode__(self):
        return self.description


class RequirementAlternativePathStep(models.Model):
    alternative_path = models.ForeignKey(RequirementAlternativePath, 
                                         verbose_name='steps')
    step_number = models.PositiveSmallIntegerField(_('Step number'))
    description = models.TextField(_('Description'))