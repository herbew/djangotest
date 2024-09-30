# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin


from djangotest.apps.myapp.models import (MyOtherModel, 
                                          MyNullableOtherModel, MyModel)


admin.site.register(MyOtherModel)
admin.site.register(MyNullableOtherModel)
admin.site.register(MyModel)
