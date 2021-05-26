pens_price = 5.80
markers_price = 7.20
detergent_l_price = 1.20
pens_packages = int(input())
markers_packages = int(input())
detergent_liters = float(input())
discount = int(input())

total = (pens_price * pens_packages + markers_price * markers_packages + detergent_l_price * detergent_liters) * (1 - discount/100)
print(f"{total:.3f}")