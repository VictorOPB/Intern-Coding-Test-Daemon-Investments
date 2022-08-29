def rs(stock_prices, lookback_period):
    gains = []
    losses = []
    lookback_prices = []
    prev_avg_gain = None
    prev_avg_loss = None
    for i, price in enumerate(stock_prices):
        if i == 0 :
            lookback_prices.append(price)
            continue
        difference = stock_prices[i] - stock_prices[i-1]
        if difference >= 0 :
            gain = difference
            loss = 0
        else:
            gain = 0
            loss = abs(difference)
        gains.append(gain)
        losses.append(loss)
        if i < lookback_period:
            lookback_prices.append(price)
            continue
        if i == lookback_period:
            avg_gain = sum(gains) / len(gains)
            avg_loss = sum(losses) / len(losses)
        else:
            avg_gain = (prev_avg_gain * (lookback_period - 1) + gain) / lookback_period
            avg_loss = (prev_avg_loss * (lookback_period - 1) + loss) / lookback_period
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss
    rs = round(avg_gain/avg_loss, 2)
    return rs