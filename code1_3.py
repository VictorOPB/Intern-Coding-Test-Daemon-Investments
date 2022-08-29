from statistics import mean
from code1_1 import *
from pf_comp import pf_comp
from rebalance import rebalance, stocks_rebalance_vol_sharpe

stock_weights = []
daily_sums = []
for i in range(years*yearly_tdays):
    daily_sums.append(np.sum(row[i] for row in best_stocks))
stock_weights = [[100*best_stocks[i][j]/daily_sums[j] for j in range(years*yearly_tdays)] for i in range(n_stocks)]

# Portfolio composition on the first day:
ini_weights = pf_comp(1, stock_weights, n_stocks)

#Rebalancing, volatility and sharpe_ratio update:
[stock_weights, best_vol, best_sharpe] = stocks_rebalance_vol_sharpe(ini_weights, stock_weights, best_stocks, best_vol, best_sharpe, n_stocks, years*yearly_tdays, lookback_period)
weights_2 = pf_comp(42, stock_weights, n_stocks)
weights_3 = pf_comp(63, stock_weights, n_stocks)

print("The necessary trades in terms of deltas on the second month are:")
trades2 = rebalance(ini_weights, weights_2, n_stocks)
for i in range(n_stocks):
    print("Trade",i,":", trades2[i])

print("The necessary trades in terms of deltas on the third month are:")
trades3 = rebalance(ini_weights, weights_3, n_stocks)
for i in range(n_stocks):
    print("Trade",i,":", trades2[i])

print("The return, volatility and sharpe ratio at the end of three months are:")
for i in range(n_stocks):
    print("Stock",i,": Return", best_returns[i][63], ", Volatility",best_vol[i], "Sharpe ratio", best_sharpe[i])