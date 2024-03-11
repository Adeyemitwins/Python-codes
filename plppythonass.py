price = int(input('Enter a price'))
discount = int(input('Enter a discount'))
discount_percentage = float(discount/price * 100)
final_price = float(price - discount_percentage)
discount_calc = float(20/100 * price)
print("The final price is:", final_price)

def calculate_discount (price, discount):
    if discount == discount_calc:
        return final_price
    print(final_price)


if discount != discount_calc:
    print(price)


calculate_discount(price, discount)