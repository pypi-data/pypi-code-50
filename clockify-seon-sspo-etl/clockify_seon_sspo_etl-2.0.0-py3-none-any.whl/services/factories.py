import factory
from clockfy_seon_sspo_etl.services.project_service import ProjectService
from clockfy_seon_sspo_etl.services.task_service import TaskService
from clockfy_seon_sspo_etl.services.team_member_service import TeamMemberService
from clockfy_seon_sspo_etl.services.time_entry_service import TimeEntryService
from clockfy_seon_sspo_etl.services.workspace_service import WorkspaceService


import factory

class ProjectServiceFactory(factory.Factory):
    class Meta:
        model = ProjectService

class TaskServiceFactory(factory.Factory):
    class Meta:
        model = TaskService

class TeamMemberServiceFactory(factory.Factory):
    class Meta:
        model = TeamMemberService

class TimeEntryServiceFactory(factory.Factory):
    class Meta:
        model = TimeEntryService

class WorkspaceServiceFactory(factory.Factory):
    class Meta:
        model = WorkspaceService