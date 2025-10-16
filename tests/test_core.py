# SPDX-FileCopyrightText: 2025-present Jitesh Sahani (JD) <jitesh.sahani@outlook.com>
#
# SPDX-License-Identifier: MIT

import pytest

from escapist.core import Escapist


@pytest.fixture
def escapist_instance():
    """Fixture for creating an Escapist instance."""
    return Escapist()


def test_run_returns_message(escapist_instance):
    result = escapist_instance.run()
    assert isinstance(result, str)
    assert "running" in result.lower()


def test_info_contains_name(escapist_instance):
    result = escapist_instance.info()
    assert escapist_instance.name in result
    assert "CLI" in result or "tool" in result


def test_custom_name():
    e = Escapist("CustomApp")
    assert "CustomApp" in e.run()
