# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.


from collections.abc import Mapping
from functools import wraps
import re

import cf_units

from iris.common import BaseMetadata
import iris.std_names


__all__ = ["CFVariableMixin"]


def _get_valid_standard_name(name):
    # Standard names are optionally followed by a standard name
    # modifier, separated by one or more blank spaces

    if name is not None:
        name_is_valid = False
        # Supported standard name modifiers. Ref: [CF] Appendix C.
        valid_std_name_modifiers = [
            "detection_minimum",
            "number_of_observations",
            "standard_error",
            "status_flag",
        ]

        valid_name_pattern = re.compile(r"""^([a-zA-Z_]+)( *)([a-zA-Z_]*)$""")
        name_groups = valid_name_pattern.match(name)

        if name_groups:
            std_name, whitespace, std_name_modifier = name_groups.groups()
            if (std_name in iris.std_names.STD_NAMES) and (
                bool(whitespace)
                == (std_name_modifier in valid_std_name_modifiers)
            ):
                name_is_valid = True

        if name_is_valid is False:
            raise ValueError("{!r} is not a valid standard_name".format(name))

    return name


class LimitedAttributeDict(dict):
    _forbidden_keys = (
        "standard_name",
        "long_name",
        "units",
        "bounds",
        "axis",
        "calendar",
        "leap_month",
        "leap_year",
        "month_lengths",
        "coordinates",
        "grid_mapping",
        "climatology",
        "cell_methods",
        "formula_terms",
        "compress",
        "add_offset",
        "scale_factor",
        "_FillValue",
    )

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        # Check validity of keys
        for key in self.keys():
            if key in self._forbidden_keys:
                raise ValueError(f"{key!r} is not a permitted attribute")

    def __eq__(self, other):
        # Extend equality to allow for NumPy arrays.
        match = set(self.keys()) == set(other.keys())
        if match:
            for key, value in self.items():
                match = value == other[key]
                try:
                    match = bool(match)
                except ValueError:
                    match = match.all()
                if not match:
                    break
        return match

    def __ne__(self, other):
        return not self == other

    def __setitem__(self, key, value):
        if key in self._forbidden_keys:
            raise ValueError(f"{key!r} is not a permitted attribute")
        dict.__setitem__(self, key, value)

    def update(self, other, **kwargs):
        # Gather incoming keys
        keys = []
        if hasattr(other, "keys"):
            keys += list(other.keys())
        else:
            keys += [k for k, v in other]

        keys += list(kwargs.keys())

        # Check validity of keys
        for key in keys:
            if key in self._forbidden_keys:
                raise ValueError(f"{key!r} is not a permitted attribute")

        dict.update(self, other, **kwargs)


class CFVariableMixin:
    @wraps(BaseMetadata.name)
    def name(self, default=None, token=None):
        return self._metadata.name(default=default, token=token)

    def rename(self, name):
        """
        Changes the human-readable name.

        If 'name' is a valid standard name it will assign it to
        :attr:`standard_name`, otherwise it will assign it to
        :attr:`long_name`.

        """
        try:
            self.standard_name = name
            self.long_name = None
        except ValueError:
            self.standard_name = None
            self.long_name = str(name)

        # Always clear var_name when renaming.
        self.var_name = None

    @property
    def standard_name(self):
        """The CF Metadata standard name for the object."""
        return self._metadata.standard_name

    @standard_name.setter
    def standard_name(self, name):
        self._metadata.standard_name = _get_valid_standard_name(name)

    @property
    def long_name(self):
        """The CF Metadata long name for the object."""
        return self._metadata.long_name

    @long_name.setter
    def long_name(self, name):
        self._metadata.long_name = name

    @property
    def var_name(self):
        """The NetCDF variable name for the object."""
        return self._metadata.var_name

    @var_name.setter
    def var_name(self, name):
        if name is not None:
            result = self._metadata.token(name)
            if result is None or not name:
                emsg = "{!r} is not a valid NetCDF variable name."
                raise ValueError(emsg.format(name))
        self._metadata.var_name = name

    @property
    def units(self):
        """The S.I. unit of the object."""
        return self._metadata.units

    @units.setter
    def units(self, unit):
        self._metadata.units = cf_units.as_unit(unit)

    @property
    def attributes(self):
        return self._metadata.attributes

    @attributes.setter
    def attributes(self, attributes):
        self._metadata.attributes = LimitedAttributeDict(attributes or {})

    @property
    def metadata(self):
        return self._metadata.values

    @metadata.setter
    def metadata(self, metadata):
        cls = self._metadata.cls
        fields = self._metadata.fields
        arg = metadata

        try:
            # Try dict-like initialisation...
            metadata = cls(**metadata)
        except TypeError:
            try:
                # Try iterator/namedtuple-like initialisation...
                metadata = cls(*metadata)
            except TypeError:
                if hasattr(metadata, "_asdict"):
                    metadata = metadata._asdict()

                if isinstance(metadata, Mapping):
                    missing = [
                        field for field in fields if field not in metadata
                    ]
                else:
                    # Generic iterable/container with no associated keys.
                    missing = [
                        field
                        for field in fields
                        if not hasattr(metadata, field)
                    ]

                if missing:
                    missing = ", ".join(
                        map(lambda i: "{!r}".format(i), missing)
                    )
                    emsg = "Invalid {!r} metadata, require {} to be specified."
                    raise TypeError(emsg.format(type(arg), missing))

        for field in fields:
            if hasattr(metadata, field):
                value = getattr(metadata, field)
            else:
                value = metadata[field]

            # Ensure to always set state through the individual mixin/container
            # setter functions.
            setattr(self, field, value)
