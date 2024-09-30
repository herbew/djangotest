# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from djangotest.apps.myapp import models, forms
from django.urls import reverse_lazy


class MyView(generic.TemplateView):
    template_name = "myapp/my_template.html"


class MyCreateView(generic.CreateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = reverse_lazy('myapp:mycreateview')


@method_decorator(login_required, name="dispatch")
class MyUpdateView(generic.UpdateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = reverse_lazy('myapp:myupdateview', kwargs={'pk':model.pk})
