# -*- coding: utf-8 -*-

"""Top-level package for fifteenrock."""

__author__ = """Rajiv Abraham"""
__email__ = 'rajiv.abraham@15rock.com'

from fifteenrock.core.core import database, load_project, get_master_data, deploy_powerBI, model_train
from fifteenrock.core.compute_client import compute
from fifteenrock.core.fr_notebook import deploy_form, _deploy_notebook, deploy_project

from fifteenrock.constants import VERSION

__version__ = VERSION
