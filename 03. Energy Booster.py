watermelon_piece_price_small = 56.00
watermelon_piece_price_big = 28.70
mango_piece_price_small = 36.66
mango_piece_price_big = 19.60
pineapple_piece_price_small = 42.10
pineapple_piece_price_big = 24.80
raspberry_piece_price_small = 20.00
raspberry_piece_price_big = 15.20
watermelon_pckg_price_big = watermelon_piece_price_big * 5
watermelon_pckg_price_small = watermelon_piece_price_small * 2
mango_pckg_price_big = mango_piece_price_big * 5
mango_pckg_price_small = mango_piece_price_small * 2
pineapple_pckg_price_big = pineapple_piece_price_big * 5
pineapple_pckg_price_small = pineapple_piece_price_small * 2
raspberry_pckg_price_big = raspberry_piece_price_big * 5
raspberry_pckg_price_small = raspberry_piece_price_small * 2
total = 0
fruit = input()
set_size = input()
quantity = int(input())
if fruit == "Watermelon":
    if set_size == "small":
        total = watermelon_pckg_price_small * quantity
    else:
        total = watermelon_pckg_price_big * quantity
elif fruit == "Mango":
    if set_size == "small":
        total = mango_pckg_price_small * quantity
    else:
        total = mango_pckg_price_big * quantity
elif fruit == "Pineapple":
    if set_size == "small":
        total = pineapple_pckg_price_small * quantity
    else:
        total = pineapple_pckg_price_big * quantity
elif fruit == "Raspberry":
    if set_size == "small":
        total = raspberry_pckg_price_small * quantity
    else:
        total = raspberry_pckg_price_big * quantity
if 400 <= total <= 1000:
    total *= 0.85
if total > 1000:
    total *= 0.5
print(f"{total:.2f} lv.")