from api.model.FdInputWrapper import FdInputWrapper


class FdInputPipe:
    """
    输入包装
    """
    def list_source_fd_codes(self):
        """
        列出所有与之关联的来源FD的code
        :return:
        """
        return self.__source_fd_codes

    def get_fd(self, fd_code):
        """
        返回一个Fd的输入代理对象
        :param fd_code:
        :return: FdInputWrapper对象
        """
        return FdInputWrapper(fd_code)
