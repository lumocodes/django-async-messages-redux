import django
from django.conf.urls import url

if django.VERSION >= (1, 8):
    from . import views

    urlpatterns = [
        url(r'^$', views.index, name='views_test'),
    ]
else:
    from django.conf.urls import patterns

    urlpatterns = patterns('',
        url(r'^$', 'tests.views.index', name='views_test'),
    )
