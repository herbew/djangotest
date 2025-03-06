
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models


class MyOtherModel(models.Model):
    number = models.IntegerField

class MyNullableOtherModel(models.Model):
    number = models.IntegerField

class MyModel(models.Model):
    name = models.CharField(max_length=30)
    other_model = models.ForeignKey(MyOtherModel, on_delete=models.CASCADE)
    nullable_other = models.ForeignKey(MyNullableOtherModel, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(blank=True)
    
    class Meta:
        app_label = 'myapp'
        verbose_name = u"MyModel"
        verbose_name_plural = u"My Models"
        unique_together = (("name", "other_model", "nullable_model" ),)
    
