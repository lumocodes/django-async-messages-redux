import django


if django.VERSION >= (2, 0):
    from . import views
    from django.urls import re_path

    urlpatterns = [
        re_path(r'^$', views.index, name='views_test'),
    ]
elif django.VERSION >= (1, 8):
    from . import views
    from django.conf.urls import url as re_path

    urlpatterns = [
        re_path(r'^$', views.index, name='views_test'),
    ]
else:
    from django.conf.urls import patterns
    from django.conf.urls import url as re_path

    urlpatterns = patterns('',
        re_path(r'^$', 'tests.views.index', name='views_test'),
    )
