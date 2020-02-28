import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import math


def printStatement(file):
    statement = pd.read_csv(file)
    statement.Heading = statement.Heading.str.replace(' ', '_')
    statement.Heading = statement.Heading.str.replace(',', '')
    statement.Heading = statement.Heading.str.replace('&', '')
    statement['Heading'] = statement['Heading'].str.lower()
    statement = statement.set_index('Heading')
    statement=statement.abs()
    print(statement)


def multiLinecharts(file,title):

    statement = pd.read_csv(file)
    statement.Breakdown = statement.Breakdown.str.replace(' ', '_')
    statement.Breakdown = statement.Breakdown.str.replace(',', '')
    statement.Breakdown = statement.Breakdown.str.replace('&', '')
    statement['Breakdown'] = statement['Breakdown'].str.lower()
    statement = statement.set_index('Breakdown')
    statement=statement.abs()

    income_statement_mForPlot = statement.T
    income_statement_mForPlot = income_statement_mForPlot.reset_index()
    income_statement_mForPlot['index']= pd.to_datetime(income_statement_mForPlot['index'])
    income_statement_mForPlot = income_statement_mForPlot.sort_values(by='index')

    columnsList = list(income_statement_mForPlot.columns.values)
    graphRowCount=math.ceil(len(income_statement_mForPlot.columns)/3)
    fig = plt.figure(figsize=(30,45))
    fig.suptitle(title, fontsize=30)

    for x in range(1, len(columnsList)):
        plotNumber = 'ax'+str(x)
        colname = income_statement_mForPlot.columns[x]

        plotNumber = fig.add_subplot(graphRowCount,3,x)
        plotNumber.set_title(colname)
        plotNumber.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot[colname])
        plt.xticks(rotation=45)

    plt.show()

def calculateMetrics(balanceSheet,incomeStatement):

    balanceSheet = pd.read_csv(balanceSheet)
    incomeStatement = pd.read_csv(incomeStatement)

    balanceSheet.Breakdown = balanceSheet.Breakdown.str.replace(' ', '_')
    balanceSheet.Breakdown = balanceSheet.Breakdown.str.replace(',', '')
    balanceSheet.Breakdown = balanceSheet.Breakdown.str.replace('&', '')
    incomeStatement.Breakdown = incomeStatement.Breakdown.str.replace(' ', '_')
    incomeStatement.Breakdown = incomeStatement.Breakdown.str.replace(',', '')
    incomeStatement.Breakdown = incomeStatement.Breakdown.str.replace('&', '')
    balanceSheet['Breakdown'] = balanceSheet['Breakdown'].str.lower()
    incomeStatement['Breakdown'] = incomeStatement['Breakdown'].str.lower()
    balanceSheet = balanceSheet.set_index('Breakdown')
    incomeStatement = incomeStatement.set_index('Breakdown')
    balanceSheet=balanceSheet.abs()
    incomeStatement=incomeStatement.abs()

    frames = [balanceSheet, incomeStatement]
    Ratio = pd.DataFrame()
    dataframeForRatio = pd.concat(frames)
    dataframeForRatio = dataframeForRatio.drop_duplicates()
    dataframeForRatio = dataframeForRatio.T
    dataframeForRatio['average_inventory'] = dataframeForRatio['inventory'].mean()
    dataframeForRatio['average_accounts_receivable'] = dataframeForRatio['net_receivables'].mean()

    #Liquidity Ratios
    Ratio['quick_ratio'] = (dataframeForRatio['cash_and_cash_equivalents']+dataframeForRatio['net_receivables']+dataframeForRatio['short_term_investments'])/dataframeForRatio['total_current_liabilities']
    Ratio['acid-test_ratio'] = dataframeForRatio['total_current_assets']/dataframeForRatio['total_current_liabilities']
    Ratio['cash_ratio'] = (dataframeForRatio['total_current_assets']-dataframeForRatio['inventory'])/dataframeForRatio['total_current_liabilities']

    #Leverage Financial Ratios
    Ratio['debt_ratio'] = dataframeForRatio['total_liabilities']/(dataframeForRatio['total_assets']-dataframeForRatio['total_liabilities'])
    Ratio['interest_coverage_ratio'] = dataframeForRatio['gross_profit']/dataframeForRatio['interest_expense']
    #Ratio['debt_service_coverage_ratio'] = dataframeForRatio['gross_profit']/dataframeForRatio['']

    #Efficiency Ratios
    Ratio['asset_turnover_ratio'] = dataframeForRatio['total_revenue']/dataframeForRatio['total_assets']
    Ratio['inventory_turnover_ratio'] = dataframeForRatio['cost_of_revenue']/dataframeForRatio['average_inventory']
    Ratio['receivables_turnover_ratio'] = dataframeForRatio['total_revenue']/dataframeForRatio['average_accounts_receivable']
    Ratio['days_sales_in_inventory_ratio'] = 365/Ratio['inventory_turnover_ratio']

    #Profitability Ratios
    Ratio['gross_margin_ratio'] = dataframeForRatio['gross_profit']/dataframeForRatio['total_revenue']
    Ratio['operating_margin_ratio'] = dataframeForRatio['net_income']/dataframeForRatio['total_revenue']
    Ratio['return_on_assets_ratio'] = dataframeForRatio['net_income']/dataframeForRatio['total_revenue']
    Ratio['return_on_equity_ratio'] = dataframeForRatio['net_income']/(dataframeForRatio['total_revenue']-dataframeForRatio['total_liabilities'])

    Ratio = Ratio.T
    Ratio = Ratio.round(4)
    print(Ratio)
