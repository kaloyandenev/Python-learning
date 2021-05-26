import re
pattern = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"
count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    barcode = input()
    product_group = ""
    if re.match(pattern, barcode):
        for char in barcode:
            if char.isdigit():
                product_group += char
        if product_group:
            print(f"Product group: {product_group}")
        else:
            product_group = "00"
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

