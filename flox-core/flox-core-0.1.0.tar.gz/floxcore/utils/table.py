from terminaltables import SingleTable


class BaseTable(SingleTable):
    def __init__(self, data):
        super().__init__(data)

        self.inner_row_border = False
        self.inner_column_border = False
        self.outer_border = False
        self.inner_heading_row_border = True
