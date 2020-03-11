import numpy as np
import pandas as pd

from immo_tools.constants import *


class UnitException(Exception):
    pass


class Calculator:
    def __init__(self):
        self.summary = None

    def get_cost(self, sales_year=8):
        if self.summary is None:
            return None
        return self.summary \
                   .groupby(by=[YEAR_COL]) \
                   .sum() \
                   .iloc[:sales_year, :] \
                   .loc[:, [INTERSET_COL, INS_ALL_COL, REFUNDED_CAP_COL]] \
            .sum() \
            .round(2)


def convert_rate_per_month(rate, n_per=12):
    return (np.power(1 + rate, 1 / n_per)) - 1


def convert_duration_in_years(dur, unit='month'):
    if unit == 'month':
        return int(dur / 12)
    elif unit == 'year':
        return int(dur)
    raise UnitException(f'unité {unit} non gérée')


class Loan(Calculator):
    summary = None

    def __init__(self, duration, amount, year_rate, insurance_rate, duration_unit='month', build_summary=False,
                 ins_on_rest=False):
        super().__init__()
        self.amount = amount
        self.insurance_rate = insurance_rate / 100
        self.duration = convert_duration_in_years(duration, duration_unit)
        self.year_rate = year_rate / 100
        self.month_rate = convert_rate_per_month(self.year_rate)
        self.monthly = self.get_monthly()
        self.ins_on_rest = ins_on_rest
        if build_summary:
            self.build_summary(ins_on_rest)

    def get_monthly(self):
        if self.month_rate == 0:
            return self.amount / self.duration / 12
        m = np.power(1 + self.month_rate, self.duration * 12)
        a = self.amount * self.month_rate * m
        b = m - 1
        return a / b

    def build_summary(self, ins_on_rest=False):
        self.summary = self.get_summary(ins_on_rest)

    def get_summary(self, ins_on_rest=False):
        summary = []
        cap = int(self.amount)
        year = 0
        for idx, period in enumerate(range(self.duration * 12)):
            if idx % 12 == 0:
                year += 1
            interest = self.month_rate * cap
            refunded_cap = self.monthly - interest
            cap = cap - refunded_cap

            a = cap if ins_on_rest else self.amount
            ins = a * (self.insurance_rate / 12)

            summary.append({
                YEAR_COL: int(year),
                MONTHLY_COL: self.monthly,
                INS_ALL_COL: ins,
                MONTHLY_INS_COL: self.monthly + ins,
                REFUNDED_CAP_COL: refunded_cap,
                INTERSET_COL: interest,
                CAP_COL: cap
            })
        return pd.DataFrame(summary)

    def get_interests(self):
        if self.summary is None:
            return None
        return self.summary.loc[:, [INTERSET_COL]].sum().round(2).values[0]


def build_loan(duration, amount, year_rate, insurance_rate, duration_unit='month', build_summary=False,
               ins_on_rest=False):
    return Loan(duration, amount, year_rate, insurance_rate, duration_unit, build_summary,
                ins_on_rest)
