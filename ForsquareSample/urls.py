from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from ForsquareSampleApp.views import access_page, parse_code, all_check_ins, all_places, notifications

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ForsquareSample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get-started/', access_page),
    url(r'^$', parse_code),
    url(r'^all-check-ins/$', all_check_ins),
    url(r'^all-places/$', all_places),
    url(r'^notifications/$', notifications),
    url(r'^st$', TemplateView.as_view(template_name='check-ins.html'))
)
