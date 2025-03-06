# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from rest_framework.routers import DefaultRouter

from django.urls import path, include

from djangotest.apps.myapp import views

router = DefaultRouter()
router.register(r'myothermodels', MyOtherModelViewSet)

app_name = 'myapp'

urlpatterns = [
    path('mypath/', view=views.MyView.as_view(), name='myview'),
    path('create/', view=views.MyCreateView.as_view(), name='mycreateview'),
    path('<int:pk>/update/', view=views.MyUpdateView.as_view(), name='myupdateview'),
    path('api/', include(router.urls))

]


# Create: POST request ke http://127.0.0.1:8000/api/myothermodels/
# Read: GET request ke http://127.0.0.1:8000/api/myothermodels/ untuk melihat semua data atau http://127.0.0.1:8000/api/items/{id}/ untuk melihat data dengan ID tertentu.
# Update: PUT atau PATCH request ke http://127.0.0.1:8000/api/myothermodels/{id}/
# Delete: DELETE request ke http://127.0.0.1:8000/api/myothermodels/{id}/