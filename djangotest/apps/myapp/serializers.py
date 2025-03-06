# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import logging
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

log = logging.getLogger(__name__)

from djangotest.apps.myapp.models import (MyOtherModel, 
                                          MyNullableOtherModel,
                                          MyModel)

class MyOtherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyOtherModel
        fields = ['id', 'number']
        
class MyNullableOtherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNullableOtherModel
        fields = ['id', 'number']
        
class MyModelSerializer(serializers.ModelSerializer):
    other_model = MyOtherModelSerializer(required=True)
    nullable_other = MyNullableOtherModelSerializer(required=True)
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'other_model', 'nullable_other', 'comment']
        
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=MyModel.objects.all(),
                fields=('name', 'other_model','nullable_other'),
                message=_("The Record with the same keys already exists!")
            )
        ]