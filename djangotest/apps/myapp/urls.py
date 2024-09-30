# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import path

from djangotest.apps.myapp import views

app_name = 'myapp'

urlpatterns = [
    path('mypath/', view=views.MyView.as_view(), name='myview'),
    path('create/', view=views.MyView.as_view(), name='mycreateview'),
    path('<int:pk>/update/', view=views.MyUpdateView.as_view(), name='myupdateview'),

]
