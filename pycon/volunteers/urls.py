from django.conf.urls import url

from pycon.volunteers.views import VolunteersView

urlpatterns = [
    url(r"^$", VolunteersView.as_view(), name='volunteers'),
]
