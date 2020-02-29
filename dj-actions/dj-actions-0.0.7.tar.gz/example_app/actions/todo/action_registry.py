# noqa
from actions.util import (
    STATUS,
    ACTION_TYPE,
    enrich_actions
)

# maybe we can just work this out from the directory?
action_list = []
# -- START ACTION REGISTRY -- #
action_list.append(('mark_done', ACTION_TYPE.INSTANCE.value, STATUS.ALPHA.value))
action_list.append(('bulk_mark_done', ACTION_TYPE.BULK.value, STATUS.ALPHA.value))
# -- END ACTION REGISTRY -- #

base = 'example_app/actions/todo'

initial_registry = {
    "resource": "todo",
    "basepath": "",
    "actions": {}
}
ACTIONS = enrich_actions(
    base,
    initial_registry,
    action_list
)
