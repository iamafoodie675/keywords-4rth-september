def dueAmount(b,g):
    return g-b

bill = int(input("Enter the bill: "))
given= int(input("Enter the given amount: "))

res = dueAmount(bill,given)
print(f"bill :{bill}\n given amount:{given}\n due amount : {res}")