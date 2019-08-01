import sys
import pytest
from matplotlib import cbook


class NoString:
    def __repr__(self):
        pass


if sys.platform == "darwin":
    from matplotlib.backends import _macosx

    def test_set_icon():
        with pytest.raises(TypeError):
            _macosx.set_icon()

        with pytest.raises(TypeError):
            _macosx.set_icon(1)

        with pytest.raises(TypeError):
            _macosx.set_icon([1, 2, 'a'])

        with pytest.raises(TypeError):
            _macosx.set_icon(None)

        with pytest.raises(TypeError):
            _macosx.set_icon(NoString())

        with pytest.raises(RuntimeError):
            _macosx.set_icon("invalid path")

        icon = cbook._get_data_path("images/matplotlib.pdf")
        _macosx.set_icon(icon)
