# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import importlib
import os
import sys
from os.path import dirname
from typing import Set

from azureml.automl.core._shared_package_legacy_import import _SharedPackageMetaPathFinder


def _handle_legacy_shared_package_imports():
    # Note: the code in the 'shared' package is used directly by some AutoML components that live in the
    # Jasmine repo. This shared package used to be importable under different namespaces.
    # For the sake of backwards compatibility (not breaking legacy code still using these imports),
    # we redirect legacy aliases to the 'shared' module they intend to reference.
    legacy_aliases = set([
        "automl.client.core.runtime",
        "azureml.automl.runtime._vendor.automl.client.core.runtime",
    ])

    # We also need to redirect selected prefixes of the legacy aliases.
    # This is because:
    # (1) The code 'import automl.client.core.runtime.x' requires all package prefixes
    #     ('automl', 'automl.client', etc.) to be valid, importable packages.
    # (2) These stub packages used to exist. In the unlikely event someone referenced them,
    #     they'll still be importable.
    legacy_stub_packages = set([
        "automl",
        "automl.client",
        "automl.client.runtime",
        "azureml.automl.runtime._vendor",
        "azureml.automl.runtime._vendor.automl",
        "azureml.automl.runtime._vendor.automl.client",
        "azureml.automl.runtime._vendor.automl.client.core"
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
