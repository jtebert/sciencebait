from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import baitgen.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'science-clickbait.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', baitgen.views.index, name='index'),
    url(r'^db', baitgen.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
