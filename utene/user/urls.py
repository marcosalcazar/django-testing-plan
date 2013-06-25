from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from user.views import UserInfoUpdateView


urlpatterns = patterns('user.views',

    url(r'user/(?P<pk>\d+)/$', login_required(UserInfoUpdateView.as_view()), name='userinfo'),

)
