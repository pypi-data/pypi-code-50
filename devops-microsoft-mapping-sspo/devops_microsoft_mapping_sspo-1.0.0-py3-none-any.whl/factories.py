import factory
from devops_microsoft_mapping_sspo.scrum_intented_development_task import ScrumIntentedDevelopmentTask
from devops_microsoft_mapping_sspo.scrum_performed_development_task import ScrumPerformedDevelopmentTask
from devops_microsoft_mapping_sspo.scrum_atomic_project import ScrumAtomicProject
from devops_microsoft_mapping_sspo.scrum_complex_project import ScrumComplexProject
from devops_microsoft_mapping_sspo.sprint import Sprint
from devops_microsoft_mapping_sspo.team_member import Teammember
from devops_microsoft_mapping_sspo.atomic_user_story import AtomicUserStory
from devops_microsoft_mapping_sspo.epic import Epic

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

class SprintFactory(factory.Factory):
    class Meta:
        model = Sprint

class TeamMemberFactory(factory.Factory):
    class Meta:
        model = Teammember

class EpicFactory(factory.Factory):
    class Meta:
        model = Epic

class AtomicUserStoryFactory(factory.Factory):
    class Meta:
        model = AtomicUserStory