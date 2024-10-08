# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestMyModel:
    def test_mymodel(self):
        my_model = mixer.blend("myapp.MyModel")
        assert my_model.pk == 1, "Should create a MyModel instance"
