from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'django_base_skeleton.views.home', name='home'),
  # url(r'^django_base_skeleton/', include('django_base_skeleton.foo.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),

  url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
  url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

  url(r'^reset_password/$', 'django.contrib.auth.views.password_reset', name='reset_password'),
  url(r'^reset_password_done/$', 'django.contrib.auth.views.password_reset_done', name='reset_password_done'),
  url(r'^reset_password_complete/$', 'django.contrib.auth.views.password_reset_complete', name='reset_password_complete'),
  url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='reset_password_confirm'),
  # at this point if you have not setup your mail settings, you will get [Errno 111] Connection refused

  url(r'^api/', include('django_base_skeleton.api.urls')), #>_<
  
  url(r'^$', 'django_base_skeleton.polls.views.home', name='home'), #>_<
  
  url(r'^foo/$', 'django_base_skeleton.polls.views.foo', name='foo'), #>_<

  url(r'^polls/$', 'django_base_skeleton.polls.views.showPolls', name='showPolls'), #>_<
  url(r'^poll/create/$', 'django_base_skeleton.polls.views.createPoll', name='createPoll'), #>_<
  url(r'^choice/create/$', 'django_base_skeleton.polls.views.createChoice', name='createChoice'), #>_<

)
