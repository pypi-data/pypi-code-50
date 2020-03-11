from itertools import chain
from collections import Counter

from .worker import WorkManager


class Dataset:
    r"""The most important class in DAME.

    Manages access, computation of dataset elements

    What you probably want to do is to subclass this class and redefine it's source
    and transforms attributes.

    Attributes:
        source (Source): As lightweight as possible data source
        transforms (Iterable[Transform_cls]): Processing of data items at element level
        store (Store_cls): Storage method to permanently save computed

    """
    source = None
    transforms = tuple()
    context = {}

    def __init__(self):
        if hasattr(self, "store"):
            self.add_arguments_for(self.store, src_id=self.source.version())

    @property
    def manager(self):
        if getattr(self, "_manager", None) is None:
            if not hasattr(self, "_validated"):
                self.validate()
                self._validated = True
            self._manager = WorkManager(
                self.source,
                self.transforms,
                self.context,
                n_processes=getattr(self, "n_processes", None),
                store=getattr(self, "store", None)
            )
        return self._manager

    def __getitem__(self, idx):
        r"""Computes a single dataset element"""
        return self.manager.compute_one(idx)

    def __len__(self):
        return len(self.manager.source_instance)

    def __iter__(self):
        r"""Returns an iterator over the dataset with all transforms applied"""
        return self.manager.fast_compute()

    def assequence(self, of=None):
        r"""Returns a sequence of `{key: computed_value for key in of}`

        Args:
            of (str|set(str), optional): the keywords to keep in each element.
                Defaults to None.
        """
        if of is None:
            return iter(self)
        return map(
            lambda data: {key: value for key, value in data.items() if key in of}, self
        )

    def set_arguments_for(self, cls, *args, **kwargs):
        r"""Provide arguments to use when creating cls instances.
        Dame will use cls(*args, **kwargs) to get an instance.

        Args:
            cls (transform | source class): Class for which params will be registered
            *args (any): list of positional args
            **kwargs (any): list of keyword args
        """
        ctx = {"args": args, "kwargs": kwargs}
        self.context[cls.__name__] = ctx
        return self

    def add_arguments_for(self, cls, *args, **kwargs):
        if cls.__name__ not in self.context:
            self.context[cls.__name__] = {}
        ctx = self.context[cls.__name__]
        ctx["args"] = ctx.get("args", []) + args
        if "kwargs" not in ctx:
            ctx["kwargs"] = {}
        ctx["kwargs"].update(kwargs)

        return self

    def validate(self):
        r"""Validates (roughly) the subclass's transforms and source

        This method is called each time a subclass of dataset is created.
        It ensures that the transforms have 'provides' attribute and
        that no provided keywords overlap.

        Args:
            self (Dataset): The new instance of Dataset
        """
        assert (
            getattr(self, "source", None) is not None
        ), "Dataset can't exist without a source. "
        repeated_keywords = [
            kw for kw, num in Counter(self._get_all_keywords()).most_common() if num > 1
        ]
        assert len(repeated_keywords) == 0, (
            "Transforms' provided keywords must be unique. "
            f"Violated by {repeated_keywords}"
        )
        return self

    def _get_all_keywords(self):
        r"""Gets all the keywords declared by a dataset.

        Args:
            obj (Dataset or cls): The dataset object or a subclass of a Dataset

        Returns:
            list(string): all keywords declared by obj.
        """

        keywords = [
            chain.from_iterable(
                [t.provides for t in chain(self.transforms, (self.source,))]
            )
        ]
        return keywords
