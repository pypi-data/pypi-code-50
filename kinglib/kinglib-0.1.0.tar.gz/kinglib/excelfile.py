#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kinglib.excel import Excel

class Excelfile:

    def __init__(self, excel_file, headers=[]):
        self._sheet = Excel(excel_file)
        self._headers = self._sheet.get_titles() if len(headers) == 0 else headers
        self._row = 1
        

    def _write_table_title(self):
        for key in self._headers:
            self._sheet.column(1, self._get_column_id(key), key)

    def _get_column_id(self, column_name):
        try:
            return self._headers.index(column_name) + 1
        except:
            return 0

    def write_excel(self, values):
        # 写表头
        if self._row == 1:
            self._write_table_title()
            self._row += 1

        # 写数据
        for index, key in enumerate(values):
            self._sheet.column(self._row, self._get_column_id(key), values[key])
            
        self._row += 1

        return self._row

    def get_row_value(self, row, key):
        return self._sheet.get_value(row, key)

    def get_title(self):
        return self._headers

    def get_rows(self):
        return self._sheet.get_rows()

    def close(self):
        self._sheet.save()