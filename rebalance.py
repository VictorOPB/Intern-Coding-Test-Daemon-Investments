from statistics import mean


import numpy as np
import pandas as pd
def rebalance(weight_ini, weight2, n_stocks):
    trades = []
    for i in range(n_stocks):
        trades.append(round(weight_ini[i] - weight2[i], 2))
    return trades

#def lookback_period_mean(lookback_period, stock_prices):

def stocks_rebalance_vol_sharpe(weight_ini, stock_weights, stock_prices, stock_vol, stock_sharpe, n_stocks, days, lookback_period):
    for i in range(days):
        for j in range(n_stocks):
            if i % lookback_period == 0:
                stock_weights[j] += rebalance(weight_ini, stock_weights[j], n_stocks)
                stock_vol[j] = np.sqrt(((stock_prices[j][i] - np.sum(stock_prices[j][(i-lookback_period) : i])/lookback_period)**2)/(lookback_period-1))
                stock_sharpe[j] = (np.sum(stock_prices[j][(i-lookback_period) : i])/lookback_period)/(1000*stock_vol[j])
    return [stock_weights, stock_vol, stock_sharpe]