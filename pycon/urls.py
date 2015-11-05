from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from pycon.home.views import HomeView
from pycon.volunteers.views import VolunteersView

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS

    url(r'^admin/', include(admin.site.urls)),
    url(r'^slides/', include('pycon.slides.urls')),
]

urlpatterns += i18n_patterns(
    url(r"^$", HomeView.as_view(), name='home'),
    url(r'^volunteers/$', VolunteersView.as_view(), name='volunteers'),

    url(r'^about/', include('pycon.about.urls')),
    url(r'^schedule/', include('pycon.schedule.urls')),
    url(r'^sponsors/', include('pycon.sponsors.urls')),
    url(r'^venue/', include('pycon.venue.urls')),
    url(r'^conduct/', include('pycon.conduct.urls')),
    url(r'^accounts/', include('allauth.urls')),
)

if getattr(settings, 'DEBUG'):
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
