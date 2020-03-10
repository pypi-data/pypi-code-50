import factory
from devops_microsoft_sspo_real_time.scrum_development_task import ScrumDevelopmentTask
from devops_microsoft_sspo_real_time.scrum_project import ScrumProject
import factory

class ScrumDevelopmentTaskFactory(factory.Factory):
    class Meta:
        model = ScrumDevelopmentTask

class ScrumProjectFactory(factory.Factory):
    class Meta:
        model = ScrumProject
