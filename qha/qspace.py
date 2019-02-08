import pandas as pd

from qha.abstractions import Axis, BiaxialField

NORMAL_MODE_LABELS = ("q", "s")


class NormalMode(Axis):
    def __init__(self, data, name, dtype=None):
        assert name in NORMAL_MODE_LABELS
        self.internal = pd.Index(data=data, dtype=dtype, name=name)


class QSpaceField(BiaxialField):
    def __init__(self, data, index: NormalMode, columns: NormalMode, dtype=None):
        assert index.name != columns.name
        assert {index.name, columns.name} not in NORMAL_MODE_LABELS
        self.internal = pd.DataFrame(data=data, index=index.internal, columns=columns.internal, dtype=dtype)
