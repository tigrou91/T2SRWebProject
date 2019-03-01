"""
Definition of urls for T2SRWebProject.
"""

from django.conf.urls import include, url
import HelloT2SRApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', T2SRWebProject.views.home, name='home'),
    # url(r'^T2SRWebProject/', include('T2SRWebProject.T2SRWebProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HelloT2SRApp.views.index, name='index'),
    url(r'^home$', HelloT2SRApp.views.index, name='home'),
    url(r'^about$', HelloT2SRApp.views.about, name='about'),
]
