# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from rest_framework import viewsets

from djangotest.apps.myapp import models, forms
from django.urls import reverse_lazy

from djangotest.apps.myapp.serializers import (
    MyOtherModelSerializer,
    MyNullableOtherModelSerializer, 
    MyModelSerializer)


class MyView(generic.TemplateView):
    template_name = "myapp/my_template.html"


class MyCreateView(generic.CreateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = reverse_lazy('myapp:myview')


@method_decorator(login_required, name="dispatch")
class MyUpdateView(generic.UpdateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = reverse_lazy('myapp:myview')


class MyOtherModelViewSet(viewsets.ModelViewSet):
    queryset = models.MyOtherModel.objects.all()
    serializer_class = MyOtherModelSerializer