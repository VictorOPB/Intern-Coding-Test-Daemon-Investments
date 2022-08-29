# To begin an approximate approach, we assume a Brownian Motion behavior regarding the daily returns,
# Which translates into a normally distributed return data.
import numpy as np
import matplotlib.pyplot as plt
from rs import rs

lookback_period = 21 # window of time used to estimate relative stock strength and volatility.
n_stocks = 10
years = 10
yearly_tdays = 252 # Number of yearly trading days is 252. Therefore, we have 21 monthly trading days.

np.random.seed(1)
mu = [0.8e-3*x for x in np.random.rand(100, 1)]
sigma = [6e-2*x for x in np.random.rand(100, 1)]
start_prices = [.50*x for x in np.random.rand(100, 1)]
stocks = []
best_stocks = []        #Selected samples after using the rs screening approach.
stock_returns = []
best_returns = []       # Returns of selected samples.
stocks_rs = {}
best_rs = []            #The first ten rs stock values from stock_rs, descending order.
stocks_vol = []         # Stocks volatility.
best_vol = []           # Stock volatility from the selected samples.
stocks_sharpe = []      # Stocks Sharpe ratio.
best_sharpe = []        # Stock Sharpe ratio from the selected samples. 

for i in range(0, len(start_prices)):
    returns = np.random.normal(loc=mu[i], scale=sigma[i], size = years*yearly_tdays)
    prices = start_prices[i]*(1+returns).cumprod()
    stocks_rs.update({i : rs(prices, lookback_period)})
    stocks_vol.append(sigma[i])
    stocks_sharpe.append(mu[i]/sigma[i])
    stocks.append(prices)
    stock_returns.append(returns)

sorted_stocks_rs = {k:v for k, v in sorted(stocks_rs.items(), key=lambda item: item[1], reverse = True)}

for i, value in sorted_stocks_rs.items():
    if len(best_stocks) < n_stocks:
        best_stocks.append(stocks[i])   # 10 rows by 2520 column
        best_returns.append(stock_returns[i])  # 10 rows by 2520 column
        best_rs.append(value)                  # 1 row by 10 columns
        best_vol.append(stocks_vol[i])         # 1 row by 10 columns
        best_sharpe.append(stocks_sharpe[i])   # 1 row by 10 columns
    else:
        break

for i in range(0, n_stocks):
    plt.plot(best_stocks[i])

plt.xlabel('Days')
plt.ylabel('Stock Price (R$)')
plt.title('Simulated Brownian Stocks')
plt.legend('0123456789')
plt.show()