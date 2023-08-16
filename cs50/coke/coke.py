amount_due=50
while amount_due>0:
    print("amount due: ", amount_due)
    coin = int (input("insert coin: "))
    if coin  in [25,10,5]:
        amount_due -=coin

changed_owed= abs(amount_due)
print("Change Owed: ", changed_owed)