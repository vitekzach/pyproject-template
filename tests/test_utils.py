"""Utils tests."""

import pytest

from project_name.core.util import return_int_back


@pytest.mark.utils
def test_return_int_back():
    """Test return in function."""
    assert isinstance(return_int_back(1), int)
    assert return_int_back(5) == 5
