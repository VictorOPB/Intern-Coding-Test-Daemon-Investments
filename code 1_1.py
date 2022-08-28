# To begin an approximate approach, we assume a Brownian Motion behavior regarding the daily returns,
# Which translates into a normally distributed return data.
import numpy as np
import matplotlib.pyplot as plt

n_stocks = 10
years = 10
yearly_tdays = 252 # Number of yearly trading days is 252.

np.random.seed(1)
mu = [2e-3*x for x in np.random.rand(10, 1)]
sigma = [4e-2*x for x in np.random.rand(10, 1)]
start_price = [.50*x for x in np.random.rand(10, 1)]
prices = []
stock_returns = []

for i in range(0, years):
    returns = np.random.normal(loc=mu[i], scale=sigma[i], size = 10*yearly_tdays)
    price = start_price[i]*(1+returns).cumprod()
    prices.append(price)
    stock_returns.append(returns)

for i in range(0, years):
    plt.plot(prices[i])
plt.xlabel('Days')
plt.ylabel('Stock Price (R$)')
plt.title('Simulated Brownian Stock')
plt.legend('ABCDEFGHIJ')
plt.show()