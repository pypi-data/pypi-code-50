import factory
from devops_microsoft_mapping_sspo.scrum_intented_development_task import ScrumIntentedDevelopmentTask
from devops_microsoft_mapping_sspo.scrum_performed_development_task import ScrumPerformedDevelopmentTask
from devops_microsoft_mapping_sspo.scrum_atomic_project import ScrumAtomicProject
from devops_microsoft_mapping_sspo.scrum_complex_project import ScrumComplexProject
import factory

class ScrumAtomicProjectFactory(factory.Factory):
    class Meta:
        model = ScrumAtomicProject

class ScrumComplexProjectFactory(factory.Factory):
    class Meta:
        model = ScrumComplexProject


class ScrumIntentedDevelopmentTaskFactory(factory.Factory):
    class Meta:
        model = ScrumIntentedDevelopmentTask

class ScrumPerformedDevelopmentTaskFactory(factory.Factory):
    class Meta:
        model = ScrumPerformedDevelopmentTask
