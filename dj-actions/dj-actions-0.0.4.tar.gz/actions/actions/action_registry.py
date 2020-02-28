# noqa
from actions.util import (
    STATUS,
    ACTION_TYPE,
    enrich_actions
)

# maybe we can just work this out from the directory?
action_list = []
# -- START ACTION REGISTRY -- #
action_list.append(('archive_actions', ACTION_TYPE.BULK.value, STATUS.ALPHA.value))
# -- END ACTION REGISTRY -- #

base = '/code/actions/'

initial_registry = {
    "resource": "actionevent",
    "basepath": "",
    "actions": {}
}
ACTIONS = enrich_actions(
    base,
    initial_registry,
    action_list
)
