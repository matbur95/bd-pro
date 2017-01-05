from django.conf.urls import url
from django.contrib.auth.views import logout

from .views import loggedin, login, registration

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^loggedin/$', loggedin, name='loggedin'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
]
