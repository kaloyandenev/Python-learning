book_pages = 899
hard_pages = 2
one_page_price = float(input())
hard_page_price = float(input())
discount = int(input())
design = float(input())
team_share_percent = int(input())

total_book_price = (one_page_price * book_pages + hard_pages * hard_page_price)
discounted_price = total_book_price * ((100 - discount) / 100)
total_price = discounted_price + design
total = total_price * ((100 - team_share_percent) / 100)
print(f"Avtonom should pay {total:.2f} BGN.")