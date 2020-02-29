# noqa
from actions.util import (
    STATUS,
    ACTION_TYPE,
    enrich_actions
)

# maybe we can just work this out from the directory?
action_list = []
# -- START ACTION REGISTRY -- #
{% for action_id, action_type, action_status in action_list %}
action_list.append(('{{action_id}}', ACTION_TYPE.{{action_type|upper}}.value, STATUS.{{action_status|upper}}.value)){% endfor %}
# -- END ACTION REGISTRY -- #

base = '{{appname|lower}}/actions/{{resource|lower}}'

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
