def profit(costprice, sellingprice):
    profit = (sellingprice-costprice)
    return profit

def loss(costprice, sellingprice):
    loss = (costprice-sellingprice)
    return loss

if __name__ == "__main__":
    costprice = int(input("Enter the cost price sucka: "))
    sellingprice = int(input("Enter the selling price sucka: "))

    if costprice == sellingprice:
        print("U got no profit nor loss.")

    elif sellingprice > costprice:
        print("Paise aaye hai!")

    else:
        print("Paise gaye hai :(")
