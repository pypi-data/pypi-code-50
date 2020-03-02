# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import importlib
import os
import sys
from os.path import dirname
from typing import Set


def _handle_legacy_shared_package_imports():
    # Note: the code in the 'shared' package is used directly by some AutoML components that live in the
    # Jasmine repo. This shared package used to be importable under different namespaces.
    # For the sake of backwards compatibility (not breaking legacy code still using these imports),
    # we redirect legacy aliases to the 'shared' module they intend to reference.
    legacy_aliases = set([
        "automl.client.core.common",
        "azureml.automl.core._vendor.automl.client.core.common",
    ])

    # We also need to redirect selected prefixes of the legacy aliases.
    # This is because:
    # (1) The code 'import automl.client.core.common.x' requires all package prefixes
    #     ('automl', 'automl.client', etc.) to be valid, importable packages.
    # (2) These stub packages used to exist. In the unlikely event someone referenced them,
    #     they'll still be importable.
    legacy_stub_packages = set([
        "automl",
        "automl.client",
        "automl.client.core",
        "azureml.automl.core._vendor",
        "azureml.automl.core._vendor.automl",
        "azureml.automl.core._vendor.automl.client",
        "azureml.automl.core._vendor.automl.client.core"
    ])

    # Find shared package's init file
    shared_module_init_file_path = os.path.join(dirname(__file__), "shared", "__init__.py")

    # Find azureml package's init file.
    # (Legacy stub package imports will be redirected to the top-level azureml stub package.)
    azureml_init_file_path = os.path.join(dirname(dirname(dirname(__file__))), "__init__.py")

    # Append the SharedPackageMetaPathFinder to the sys.meta_path
    sys.meta_path.append(_SharedPackageMetaPathFinder(
        legacy_aliases,
        legacy_stub_packages,
        shared_module_init_file_path,
        azureml_init_file_path
    ))


class _SharedPackageMetaPathFinder(importlib.abc.MetaPathFinder):
    """Meta path finder that redirects legacy shared and stub package imports."""

    def __init__(
        self,
        legacy_aliases: Set[str],
        legacy_stub_packages: Set[str],
        shared_module_init_file_path: str,
        azureml_init_file_path: str
    ) -> None:
        self._legacy_aliases = legacy_aliases
        self._legacy_stub_packages = legacy_stub_packages
        self._shared_module_init_file_path = shared_module_init_file_path
        self._azureml_init_file_path = azureml_init_file_path

    def find_spec(self, fullname, path, target=None):
        """Implement find_spec method of abstract importlib.abc.MetaPathFinder base class."""
        if fullname in self._legacy_aliases:
            return importlib.util.spec_from_file_location(fullname, self._shared_module_init_file_path)
        if fullname in self._legacy_stub_packages:
            return importlib.util.spec_from_file_location(fullname, self._azureml_init_file_path)
        return None
