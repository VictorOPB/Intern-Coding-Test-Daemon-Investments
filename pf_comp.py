def pf_comp(days, stock_weights, n_stocks):
    weights_sum = 0
    weights = []
    N = days 
    print("Portfolio Composition, day", N,":")
    for i in range(n_stocks):
        weights_sum += stock_weights[i][N-1]
        print("Stock", i, ":", round(stock_weights[i][N-1], 2))
        weights.append(round(stock_weights[i][N-1],2))
    print("Sum of weights:", round(weights_sum, 2))
    return weights