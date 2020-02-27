from collections import deque

from dagster import check
from dagster.core.definitions.pipeline import PipelineDefinition
from dagster.core.definitions.resource import ScopedResourcesBuilder
from dagster.core.errors import (
    DagsterResourceFunctionError,
    DagsterUserCodeExecutionError,
    user_code_error_boundary,
)
from dagster.core.execution.plan.objects import StepInputSourceType
from dagster.core.log_manager import DagsterLogManager
from dagster.core.storage.pipeline_run import PipelineRun
from dagster.core.system_config.objects import EnvironmentConfig
from dagster.utils import EventGenerationManager, ensure_gen

from .context.init import InitResourceContext


def resource_initialization_manager(
    pipeline_def, environment_config, pipeline_run, log_manager, resource_keys_to_init,
):
    generator = resource_initialization_event_generator(
        pipeline_def, environment_config, pipeline_run, log_manager, resource_keys_to_init,
    )
    return EventGenerationManager(generator, ScopedResourcesBuilder)


def resource_initialization_event_generator(
    pipeline_def, environment_config, pipeline_run, log_manager, resource_keys_to_init
):
    check.inst_param(pipeline_def, 'pipeline_def', PipelineDefinition)
    check.inst_param(environment_config, 'environment_config', EnvironmentConfig)
    check.inst_param(pipeline_run, 'pipeline_run', PipelineRun)
    check.inst_param(log_manager, 'log_manager', DagsterLogManager)
    check.set_param(resource_keys_to_init, 'resource_keys_to_init', of_type=str)

    resource_instances = {}
    mode_definition = pipeline_def.get_mode_definition(pipeline_run.mode)
    resource_managers = deque()
    generator_closed = False

    try:
        for resource_name, resource_def in sorted(mode_definition.resource_defs.items()):
            if not resource_name in resource_keys_to_init:
                continue
            resource_context = InitResourceContext(
                pipeline_def=pipeline_def,
                resource_def=resource_def,
                resource_config=environment_config.resources.get(resource_name, {}).get('config'),
                run_id=pipeline_run.run_id,
                log_manager=log_manager,
            )
            manager = single_resource_generation_manager(
                resource_context, resource_name, resource_def
            )
            for event in manager.generate_setup_events():
                if event:
                    yield event
            initialized_resource = check.inst(manager.get_object(), InitializedResource)
            resource_instances[resource_name] = initialized_resource.resource
            resource_managers.append(manager)

        yield ScopedResourcesBuilder(resource_instances)
    except GeneratorExit:
        # Shouldn't happen, but avoid runtime-exception in case this generator gets GC-ed
        # (see https://amir.rachum.com/blog/2017/03/03/generator-cleanup/).
        generator_closed = True
        raise
    finally:
        if not generator_closed:
            error = None
            while len(resource_managers) > 0:
                manager = resource_managers.pop()
                try:
                    for event in manager.generate_teardown_events():
                        yield event
                except DagsterUserCodeExecutionError as dagster_user_error:
                    error = dagster_user_error
            if error:
                raise error


class InitializedResource(object):
    ''' Utility class to wrap the untyped resource object emitted from the user-supplied
    resource function.  Used for distinguishing from the framework-yielded events in an
    `EventGenerationManager`-wrapped event stream.
    '''

    def __init__(self, obj):
        self.resource = obj


def single_resource_generation_manager(context, resource_name, resource_def):
    generator = single_resource_event_generator(context, resource_name, resource_def)
    return EventGenerationManager(generator, InitializedResource)


def single_resource_event_generator(context, resource_name, resource_def):
    try:
        msg_fn = lambda: 'Error executing resource_fn on ResourceDefinition {name}'.format(
            name=resource_name
        )
        with user_code_error_boundary(DagsterResourceFunctionError, msg_fn):
            try:
                resource_or_gen = resource_def.resource_fn(context)
                gen = ensure_gen(resource_or_gen)
                resource = next(gen)
                yield InitializedResource(resource)
            except StopIteration:
                check.failed(
                    'Resource generator {name} must yield one item.'.format(name=resource_name)
                )
            try:
                next(gen)
            except StopIteration:
                pass
            else:
                check.failed(
                    'Resource generator {name} yielded more than one item.'.format(
                        name=resource_name
                    )
                )
    except DagsterUserCodeExecutionError as dagster_user_error:
        raise dagster_user_error


def get_required_resource_keys_to_init(execution_plan, system_storage_def):
    resource_keys = set()

    resource_keys = resource_keys.union(system_storage_def.required_resource_keys)

    for step_key, step in execution_plan.step_dict.items():
        if step_key not in execution_plan.step_keys_to_execute:
            continue
        resource_keys = resource_keys.union(
            get_required_resource_keys_for_step(
                step, execution_plan.pipeline_def, system_storage_def
            )
        )

    return frozenset(resource_keys)


def get_required_resource_keys_for_step(execution_step, pipeline_def, system_storage_def):
    resource_keys = set()

    # add all the system storage resource keys
    resource_keys = resource_keys.union(system_storage_def.required_resource_keys)
    solid_def = pipeline_def.get_solid(execution_step.solid_handle).definition

    # add all the solid compute resource keys
    resource_keys = resource_keys.union(solid_def.required_resource_keys)

    # add input type and input hydration config resource keys
    for step_input in execution_step.step_inputs:
        resource_keys = resource_keys.union(step_input.runtime_type.required_resource_keys)
        if (
            step_input.source_type == StepInputSourceType.CONFIG
            and step_input.runtime_type.input_hydration_config
        ):
            resource_keys = resource_keys.union(
                step_input.runtime_type.input_hydration_config.required_resource_keys()
            )

    # add output type and output materialization config resource keys
    for step_output in execution_step.step_outputs:
        resource_keys = resource_keys.union(step_output.runtime_type.required_resource_keys)
        if (
            step_output.should_materialize
            and step_output.runtime_type.output_materialization_config
        ):
            resource_keys = resource_keys.union(
                step_output.runtime_type.output_materialization_config.required_resource_keys()
            )

    # add all the storage-compatible plugin resource keys
    for runtime_type in solid_def.all_runtime_types():
        for auto_plugin in runtime_type.auto_plugins:
            if auto_plugin.compatible_with_storage_def(system_storage_def):
                resource_keys = resource_keys.union(auto_plugin.required_resource_keys())

    return frozenset(resource_keys)
