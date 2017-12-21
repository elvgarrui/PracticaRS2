from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'PracticaRS2.views.inicial', name='inicial'),
    url(r'^tusArtistas/', include('PracticaRS2.views.tusartistas')),
    url(r'^topEscuchado/', include('PracticaRS2.views.topartistas')),
    url(r'^descubre/', include('PracticaRS2.views.descubre')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
