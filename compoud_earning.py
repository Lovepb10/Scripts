"""
    Developer: Lovepreet Singh
    Date: March 6, 2023
    Description: calculate compound earning for shares.

    Cons:
        1. No user input (Just hard code data input)
"""


def future_prediction(price_per_share_while_purchasing, price_per_share_while_selling, invested_amount, number_of_times, additional_investment=0):

    print("\nPrice per share while purchasing : $ " +
          str(price_per_share_while_purchasing))
    print("Price per share while selling : $ " +
          str(price_per_share_while_selling))
    print("Invested amount at start: $ " + str(invested_amount))
    print("# of shares at start: " +
          str(round(invested_amount/price_per_share_while_purchasing, 2)))
    print("# of intervals : " + str(number_of_times))

    growth_rate = round(((price_per_share_while_selling -
                        price_per_share_while_purchasing)/price_per_share_while_selling) * 100, 2)
    print("Growth rate: " + str(growth_rate) + " %\n")

    mature_amount = invested_amount

    for x in range(1, (number_of_times+1)):
        if x > 1:
            mature_amount = round(mature_amount+additional_investment, 2)
        profit = round(mature_amount*(growth_rate/100), 2)
        mature_amount = round(mature_amount+profit, 2)
        invested_amount = round(
            invested_amount+additional_investment, 2)
        print(str(x) + " : " + str(mature_amount) + " | Profit : " + str(profit) +
              " | Shares : " + str(round(mature_amount/price_per_share_while_purchasing, 2)) + " | Next Investment : " + str(round(mature_amount+additional_investment, 2)))

    print("\nTotal Invested amount : $ " + str(invested_amount))
    print("Mature amount : $ " + str(mature_amount))
    print("Overall profit : $ " +
          str(round(mature_amount-invested_amount, 2)) + "\n")


if __name__ == "__main__":

    # future_prediction(1, 1.10, 100000, 24, 2000)  # AI
    # future_prediction(1, 1.10, 500, 24, 2500)  # AI
    # future_prediction(1, 1.10, 100000, 24, 2000)  # AI
    # future_prediction(1, 1.10, 500, 120, 2000)  # AI
    # future_prediction(0.57, 0.58, 400, 1)  # food
    # future_prediction(3, 3.10, 400, 1)  # weed
    # future_prediction(3, 3.50, 400, 1)  # weed
    # future_prediction(2.70, 3.50, 900, 1)  # weed
    #     future_prediction(126, 127, 400, 1) #bmo
    #     future_prediction(8.20, 8.40, 400, 1) #coneplex
    # future_prediction(20.30, 20.40, 20000, 30)
