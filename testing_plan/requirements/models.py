from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext as _


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
        return reverse_lazy('requirements:requirement_update', 
                            kwargs={'pk': self.pk})
        
    def get_absolute_delete_url(self):
        return reverse_lazy('requirements:requirement_delete', 
                            kwargs={'pk': self.pk})
