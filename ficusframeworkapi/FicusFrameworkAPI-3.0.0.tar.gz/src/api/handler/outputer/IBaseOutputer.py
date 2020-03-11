from api.model import OutputWrapper


class IBaseOutputer:

    def put_in_cache(self, code, insert_cache: dict, update_cache, upsert_cache, output_fd, poll: OutputWrapper):
        pass

    def flush_cache(self, code, insert_cache, update_cache, upsert_cache):
        """
        把缓存中的数据 发送到FD中
        :param code:
        :param insert_cache:
        :param update_cache:
        :param upsert_cache:
        :return:
        """

    def find_output_fd(self, output_fds: list, index: int):
        """
        从多个fd中,找到需要的那个fd
        :param output_fds:
        :param index:
        :return:
        """

    def is_killed(self):
        """
        判断是否已经被杀掉了
        :return:
        """
        return False
