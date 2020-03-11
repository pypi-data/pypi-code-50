import pandas as pd



df = pd.read_csv('F:/Models/relativemomentummodel.csv')
df.columns = df.columns.str.strip()
start = 12


#model's risk statistics
#*this should use "Model" column

#define (how many periods in a year)
periods = 12

def cagr():
    start_portfolio = df['S&P 500'].iloc[start]
    end_portfolio = df['S&P 500'].iloc[-1]
    years = (df['S&P 500'].count()+1-start)/periods
    model_return = (end_portfolio/start_portfolio)**(1/years)-1
    print(model_return)

def net_profit():
    start_portfolio = df['S&P 500'].iloc[start]
    end_portfolio = df['S&P 500'].iloc[-1]
    total_return = end_portfolio/start_portfolio-1
    print(total_return)

def buy_hold():
    start_buy_hold = df['S&P 500'].iloc[start]
    end_buy_hold = df['S&P 500'].iloc[-1]
    years = (df['S&P 500'].count()+1-start)/periods
    buy_hold_return = (end_buy_hold/start_buy_hold)**(1/years)-1
    print(buy_hold_return)



def sharpe():
    df['Sharpe'] = df['S&P 500'].pct_change()-((1+df['3 month Treasury yield'])**(1/periods)-1)
    sharpe_mean = df['Sharpe'][start:].mean()
    sharpe_deviation = df['Sharpe'][start:].std()
    sharpe_number = (sharpe_mean/sharpe_deviation)*(periods**0.5)
    print(sharpe_number)

def max_drawdown():
    df['Drawdown'] = df['S&P 500']/df['S&P 500'].cummax()-1
    drawdown = df['Drawdown'].min()
    print(drawdown)
