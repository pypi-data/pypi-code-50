# -*- coding: utf-8 -*-
import logging

from spaceone.core.manager import BaseManager
from spaceone.inventory.model.job_model import Job

_LOGGER = logging.getLogger(__name__)


class JobManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_model: Job = self.locator.get_model('Job')

    def list_jobs(self, query):
        return self.job_model.query(**query)
