one_bitcoin_in_leva = 1168
one_uan_in_dollars = 0.15
one_dollar_in_leva = 1.76
one_euro_in_leva = 1.95
bitcoins_in_hand = int(input())
uan_in_hand = float(input())
commission = float(input())
bitcoins_in_euro = bitcoins_in_hand * one_bitcoin_in_leva / one_euro_in_leva
uan_in_euro = uan_in_hand * one_uan_in_dollars * one_dollar_in_leva / one_euro_in_leva
total = (bitcoins_in_euro + uan_in_euro) * (1 - (commission / 100))
print(f"{total:.2f}")