import logging
import os

from pathlib import Path
from multiprocessing.managers import BaseManager
from multiprocessing.context import AuthenticationError


class QueueManager(BaseManager): pass

class RPCScheduler(object):
    CACHE_FILE = Path.home() / ".pypyr-scheduler-cli"

    def __init__(self, host="localhost", port=12345):        
        self._conn = None
        self.host = host
        self.port = port
        self.logger = logging.getLogger("pyrsched.rpc-client")
        self._previous_job_id = None

    def get_previous_job_id(self):
        if not self._previous_job_id:
            self._load_previous_job_id()
        return self._previous_job_id

    def set_previous_job_id(self, job_id):
        self._previous_job_id = job_id
        self._store_previous_job_id()

    previous_job_id = property(fget=get_previous_job_id, fset=set_previous_job_id)

    def _store_previous_job_id(self):
        with open(self.CACHE_FILE, "w") as outfile:
            outfile.write(str(self._previous_job_id))

    def _load_previous_job_id(self):
        with open(self.CACHE_FILE, "r") as infile:
            self._previous_job_id = infile.read()

    def _interpolate_job_id(self, job_id):
        if job_id == "-":
            # special case: use the stored job_id if it was stored before:
            if not self.previous_job_id:
                self.logger.error("No previous job id found.")
                raise ValueError("No previous job id found.")
            job_id = self.previous_job_id
            self.logger.debug(f"using previous job_id {job_id}")
        return job_id

    def connect(self):
        authkey = os.environ.get("PYRSCHED_SECRET", "")
        try:
            QueueManager.register("scheduler")
            m = QueueManager(address=(self.host, self.port), authkey=authkey.encode("utf-8"))
            m.connect()
            self._scheduler = m.scheduler()
        except AuthenticationError as ae:
            self.logger.error("Authentication error, are you using the correct shared secret (PYRSCHED_SECRET env variable)?")
            self.logger.error(authkey)
            raise ae

    @property
    def state(self):   
        state = self._scheduler.state()  
        return state 

    def list_jobs(self):
        job_list = self._scheduler.list_jobs()
        return job_list

    def get_job(self, job_id):
        self.logger.debug(f"get_job({job_id})")
        job_id = self._interpolate_job_id(job_id)
        job = self._scheduler.get_job(job_id)
        return job

    def add_job(self, pipeline_filename, interval):
        self.logger.debug(f"add_job({pipeline_filename}, {interval})")
        job_id = self._scheduler.add_job(pipeline_filename, interval)
        self.previous_job_id = job_id
        return job_id

    def reschedule_job(self, job_id, interval):
        self.logger.debug(f"rescheduler_job({job_id}, {interval})")
        job_id = self._interpolate_job_id(job_id)
        job = self._scheduler.reschedule_job(job_id, interval)
        return job

    def start_job(self, job_id):
        self.logger.debug(f"start_job({job_id})")
        job_id = self._interpolate_job_id(job_id)
        job = self._scheduler.start_job(job_id)
        return job 

    def stop_job(self, job_id):
        self.logger.debug(f"stop_job({job_id})")
        job_id = self._interpolate_job_id(job_id)
        job = self._scheduler.pause_job(job_id)
        return job
    
    def remove_job(self, job_id):
        self.logger.debug(f"exposed_remove_job({job_id})")
        job_id = self._interpolate_job_id(job_id)
        job = self._scheduler.remove_job(job_id)
        return job_id
