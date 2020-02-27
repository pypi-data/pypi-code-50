import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def printStatement(file):
    statement = pd.read_csv(file)
    statement.Heading = statement.Heading.str.replace(' ', '_')
    statement.Heading = statement.Heading.str.replace(',', '')
    statement.Heading = statement.Heading.str.replace('&', '')
    statement['Heading'] = statement['Heading'].str.lower()
    statement = statement.set_index('Heading')
    statement=statement.abs()
    print(statement)


def multiLinecharts(file):
    statement = pd.read_csv(file)
    statement.Heading = statement.Heading.str.replace(' ', '_')
    statement.Heading = statement.Heading.str.replace(',', '')
    statement.Heading = statement.Heading.str.replace('&', '')
    statement['Heading'] = statement['Heading'].str.lower()
    statement = statement.set_index('Heading')
    statement=statement.abs()

    income_statement_mForPlot = statement.T
    income_statement_mForPlot = income_statement_mForPlot.reset_index()
    income_statement_mForPlot['index']= pd.to_datetime(income_statement_mForPlot['index'])
    income_statement_mForPlot = income_statement_mForPlot.sort_values(by='index')

    fig = plt.figure(figsize=(30,40))

    fig.suptitle('Income Statement 12 Month Analysis',
                 fontsize=20)

    ax1 = fig.add_subplot(431)
    ax1.set_title('total_sales')
    ax1.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['total_sales'])
    plt.xticks(rotation=45)

    ax2 = fig.add_subplot(432)
    ax2.set_title('total_cost_of_goods_sold')
    ax2.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['total_cost_of_goods_sold'])
    plt.xticks(rotation=45)

    ax3 = fig.add_subplot(433)
    ax3.set_title('gross_profit')
    ax3.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['gross_profit'])
    plt.xticks(rotation=45)

    ax4 = fig.add_subplot(434)
    ax4.set_title('total_operating_expense')
    ax4.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['total_operating_expense'])
    plt.xticks(rotation=45)

    ax5 = fig.add_subplot(435)
    ax5.set_title('total_depreciation')
    ax5.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['total_depreciation'])
    plt.xticks(rotation=45)

    ax6 = fig.add_subplot(436)
    ax6.set_title('income_from_operation')
    ax6.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['income_from_operation'])
    plt.xticks(rotation=45)

    ax1 = fig.add_subplot(437)
    ax1.set_title('total_interest_expense')
    ax1.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['total_interest_expense'])
    plt.xticks(rotation=45)

    ax2 = fig.add_subplot(438)
    ax2.set_title('ebit')
    ax2.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['ebit'])
    plt.xticks(rotation=45)

    ax3 = fig.add_subplot(439)
    ax3.set_title('total_income_tax_expense')
    ax3.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['total_income_tax_expense'])
    plt.xticks(rotation=45)

    ax4 = fig.add_subplot(4,3,10)
    ax4.set_title('net_earnings')
    ax4.plot(income_statement_mForPlot['index'],
             income_statement_mForPlot['net_earnings'])
    plt.xticks(rotation=45)

    plt.show()
