# noqa
from actions.util import (
    STATUS,
    ACTION_TYPE,
    enrich_actions
)

# maybe we can just work this out from the directory?
action_list = []
# -- START ACTION REGISTRY -- #
# -- END ACTION REGISTRY -- #

base = '{{code_path}}'

initial_registry = {
    "resource": "{{resource|lower}}",
    "basepath": "{{base_path}}",
    "actions": {}
}
ACTIONS = enrich_actions(
    base,
    initial_registry,
    action_list
)
