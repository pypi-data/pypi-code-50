class BaseList(object):

    def remove_null(self, lists):
        """
        清除列表的所有空字符串
        :param lists:
        :return:
        """
        return [r for r in lists if r != ""]

