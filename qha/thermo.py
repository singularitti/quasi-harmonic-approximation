import pandas as pd

from qha.abstractions import Axis, BiaxialField

NATURAL_VARIABLE_LABELS = ("T", "S", "P", "V")
CONJUGATE_PAIRS = ({"T", "S"}, {"P", "V"})


class NaturalVariable(Axis):
    def __init__(self, data, name, dtype=None):
        assert name in NATURAL_VARIABLE_LABELS
        self.internal = pd.Index(data=data, dtype=dtype, name=name)


class ThermodynamicField(BiaxialField):
    def __init__(self, data, index: NaturalVariable, columns: NaturalVariable, dtype=None):
        assert index.name != columns.name
        assert {index.name, columns.name} not in CONJUGATE_PAIRS
        self.internal = pd.DataFrame(data=data, index=index.internal, columns=columns.internal, dtype=dtype)
