from abc import ABC


class Axis(ABC):
    @property
    def name(self):
        return self.internal.name

    @property
    def dtype(self):
        return self.internal.dtype

    @property
    def hasnans(self):
        return self.internal.hasnans

    @property
    def shape(self):
        return self.internal.shape

    @property
    def size(self):
        return self.internal.size

    @property
    def __len__(self):
        return self.internal.__len__

    @property
    def values(self):
        return self.internal.values

    def all(self, *args, **kwargs):
        return self.internal.all(*args, **kwargs)


class BiaxialField(ABC):
    @property
    def axisnames(self):
        return self.index.name, self.columns.name

    def whichaxis(self, s: str):
        names = self.axisnames
        assert s in names
        if s == names[0]:
            return 1
        return 2

    @property
    def axes(self):
        return self.internal.axes

    @property
    def columns(self):
        return self.internal.columns

    @property
    def dtypes(self):
        return self.internal.dtypes

    @property
    def index(self):
        return self.internal.index

    @property
    def shape(self):
        return self.internal.shape

    @property
    def size(self):
        return self.internal.size

    @property
    def values(self):
        return self.internal.values
