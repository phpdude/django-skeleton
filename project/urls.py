from django.conf.urls import patterns, include, url
from django.contrib import admin

from macrosurl import url


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('admin/', include(admin.site.urls)),
)
