# -*- coding: utf-8 -*-
"""Tests for mailroom module."""

import pytest


DONOR_DICT_TABLE = {
     'Linus Torvalds': [100, 150, 250],
     'Jane Goodall': [200, 250, 50],
     'Bob Ross': [1000, 550, 18],
}


@pytest.mark.parametrize('', DONOR_DICT_TABLE)
def test_report():
    from mailroom import report
    assert report() == DONOR_DICT_TABLE
