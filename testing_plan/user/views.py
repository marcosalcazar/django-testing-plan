from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.edit import UpdateView
from user.forms import UserForm


class UserInfoUpdateView(UpdateView):
    model = User
    form_class = UserForm
    
    def get_success_url(self):
        return reverse_lazy("user:userinfo", kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, _("User Information updated"))
        return UpdateView.form_valid(self, form)