from polytropos.ontology.context import Context
from polytropos.ontology.task import Task
import logging
import polytropos.actions

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

polytropos.actions.register_all()

with Context.build("/dmz/github/analysis/etl5", "/Volumes/Bulk/tmp",
                   input_dir="/mnt/composites/tmp/hutton/1_debug",
                   temp_dir="/mnt/composites/tmp/_", output_dir="/mnt/composites/tmp/hutton/org_report",
                   process_pool_chunk_size=1, steppable_mode=True) as context:
    task = Task.build(context, "clients/hutton/diagnostic")
    task.run()
