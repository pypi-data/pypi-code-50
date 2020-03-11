from abc import abstractmethod


class IProgressAble:

    @abstractmethod
    def get_task_log_id(self):
        """
        获取任务的ID
        :return:
        """
        pass

    def update_task_progress(self, progress: float):
        """
        更新任务的进度
        :return:
        """
