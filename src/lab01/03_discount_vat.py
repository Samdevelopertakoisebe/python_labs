price, discount, vat = [int(input()) for _ in range(3)]
base = price * (1 - discount/100)
vat_amount = base * vat / 100
total = base + vat_amount
print('База после скидки:', round(base, 2))
print('НДС:              ', round(vat_amount, 2))
print('Итого к оплате:   ', round(total, 2))