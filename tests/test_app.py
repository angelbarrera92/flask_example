# -*- coding: utf-8 -*-
"""
test_app
----------------------------------
Tests for `flask_example.app` module.
"""

from flask_example.app import sample_endpoint


def test_sample_endpoint():
    body, status_code = sample_endpoint()
    assert status_code == 200
