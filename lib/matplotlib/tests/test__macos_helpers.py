import sys
import pytest
from matplotlib.backends import _macos_helpers
from matplotlib import cbook


class NoString:
    def __repr__(self):
        pass


if sys.platform == "darwin":
    def test_set_mac_icon():
        with pytest.raises(TypeError):
            _macos_helpers.set_mac_icon()

        with pytest.raises(TypeError):
            _macos_helpers.set_mac_icon(1)

        with pytest.raises(TypeError):
            _macos_helpers.set_mac_icon([1, 2, 'a'])

        with pytest.raises(TypeError):
            _macos_helpers.set_mac_icon(None)

        with pytest.raises(TypeError):
            _macos_helpers.set_mac_icon(NoString())

        with pytest.raises(RuntimeError):
            _macos_helpers.set_mac_icon("invalid path")

        icon = cbook._get_data_path("images/matplotlib.pdf")
        _macos_helpers.set_mac_icon(icon)
else:
    def test_set_mac_icon():
        icon = cbook._get_data_path("images/matplotlib.pdf")
        _macos_helpers.set_mac_icon(icon)
