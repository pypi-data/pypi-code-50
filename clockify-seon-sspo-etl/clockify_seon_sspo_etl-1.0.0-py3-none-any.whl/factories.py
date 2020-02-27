import factory
from clockfy_seon_sspo_etl.atomic_software_project import AtomicSoftwareProject
from clockfy_seon_sspo_etl.complex_software_project import ComplexSoftwareProject
from clockfy_seon_sspo_etl.scrum_performed_task import ScrumPerformedTask
from clockfy_seon_sspo_etl.stakeholder_participation import StakeholderParticipation
from clockfy_seon_sspo_etl.team_member import TeamMember


import factory

class AtomicSoftwareProjectFactory(factory.Factory):
    class Meta:
        model = AtomicSoftwareProject

class ComplexSoftwareProjectFactory(factory.Factory):
    class Meta:
        model = ComplexSoftwareProject

class ScrumPerformedTaskFactory(factory.Factory):
    class Meta:
        model = ScrumPerformedTask

class StakeholderParticipationFactory(factory.Factory):
    class Meta:
        model = StakeholderParticipation

class TeamMemberFactory(factory.Factory):
    class Meta:
        model = TeamMember