# -*- coding: utf-8 -*-

class WorkflowStageDefinitionReference(object):
	"""
	Points to a StageDefinition which is to be executed with a specified
	priority. Also contains information on the last execution of this specific
	reference to a StageDefinition. Multiple references to the same
	StageDefinition may coexist in the same Workflow.
	"""

	def __init__(self, workflow_id, workflow_stage_run_level, stage_definition_id, type):
		self.workflow_id = workflow_id;
		self.workflow_stage_run_level = workflow_stage_run_level;
		self.stage_definition_id = stage_definition_id;
		self.type = type;


	"""
	Unique StageDefinition reference ID on an Workflow.
	"""
	workflow_stage_id = None;

	"""
	Unique Workflow ID.
	"""
	workflow_id = None;

	"""
	Lowest is first to be executed. Multiple WorkflowStageDefinitionReference
	items with the same workflow_id having the same run level will be executed
	in parallel. StageDefinition items of the WorkflowReference type are
	unwrapped recursively in-place before execution or when added to an
	infrastructure deploy which means that adding, removing or reordering
	StageDefinition references will have no effect on an ongoing Workflow
	execution.
	"""
	workflow_stage_run_level = None;

	"""
	Unique StageDefinition ID.
	"""
	stage_definition_id = None;

	"""
	Information on the last run. May be of any type and have any properties if
	an object. These properties may be present: successMessage:string|null,
	successMessageTimestamp:string|null, errorMessage:string|null,
	errorMessageTimestamp:string|null
	"""
	workflow_stage_exec_output_json = None;

	"""
	The schema type.
	"""
	type = None;
