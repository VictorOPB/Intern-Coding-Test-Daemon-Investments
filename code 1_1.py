# To begin an approximate approach, we assume a Brownian Motion behavior regarding the daily returns, which translates into a normally distributed return data.
# Which translates into a normally distributed return data.
import numpy as np
import matplotlib.pyplot as plt

mu = 1e-3
sigma = 1e-2
start_price = .50

np.random.seed(1)
returns = np.random.normal(loc=mu, scale=sigma, size = 3650)
price = start_price*(1+returns).cumprod()
plt.plot(price)
plt.xlabel('Days')
plt.ylabel('Stock Price (R$)')
plt.title('Simulated Brownian Stock')
plt.show()